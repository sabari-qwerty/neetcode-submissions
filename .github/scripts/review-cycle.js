// Shared logic for the LeetCode Review Cycle workflows (main.yml + schedule.yml).
//
// Cycle (one issue per problem, tracked on the project board):
//   submit 1 -> stage:day3  (next review +3 days)   learn and solve
//   submit 2 -> stage:day5  (next review +5 days)   struggle, learn and solve
//   submit 3 -> stage:day7  (next review +7 days)   struggle and solve
//   submit 4 -> stage:day30 (next review +30 days)  struggle and solve
//   submit 5 -> stage:done  (issue closed)          struggle and solve
// The daily schedule moves a card to status:due once its review date arrives.
// Submits made before the review date are ignored.

// the board is looked up by owner + number (github.com/users/sabari-qwerty/projects/6)
// and its title is checked, so the workflow can never touch a different project.
// Column option ids are resolved by name at runtime.
const PROJECT_NUMBER = 6;
const PROJECT_TITLE = "LeetCode Review Cycle";
const STATUS_FIELD = "Status";

const STAGES = [
  { name: "stage:day3", days: 3 },
  { name: "stage:day5", days: 5 },
  { name: "stage:day7", days: 7 },
  { name: "stage:day30", days: 30 },
];
const DONE = { name: "stage:done" };
const DUE = { name: "status:due" };
const TOTAL_REVIEWS = STAGES.length + 1; // 5th submit finishes the cycle

// dates are YYYY-MM-DD in IST so they match the local day
const IST_OFFSET_MS = 5.5 * 60 * 60 * 1000;
const today = () => new Date(Date.now() + IST_OFFSET_MS).toISOString().slice(0, 10);
const addDays = (date, days) => {
  const d = new Date(`${date}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() + days);
  return d.toISOString().slice(0, 10);
};

// hidden metadata stored in the issue body
const META_KEYS = ["review-count", "first-submitted", "last-submitted", "review-due", "history"];

const parseMeta = (body = "") => {
  const meta = {};
  for (const key of META_KEYS) {
    const match = body && body.match(new RegExp(`<!--\\s*${key}:\\s*([^>]*?)\\s*-->`));
    if (match) meta[key] = match[1];
  }
  return {
    count: Number(meta["review-count"] || 0),
    firstSubmitted: meta["first-submitted"] || null,
    lastSubmitted: meta["last-submitted"] || null,
    reviewDue: meta["review-due"] || null,
    history: meta["history"] ? meta["history"].split(",").filter(Boolean) : [],
  };
};

const neetcodeUrl = (slug) => `https://neetcode.io/problems/${slug}/question`;

const renderBody = (slug, meta) => {
  const done = meta.count >= TOTAL_REVIEWS;
  const lines = [
    `**Problem:** ${slug}`,
    `**Neetcode URL:** ${neetcodeUrl(slug)}`,
    `**First submitted:** ${meta.firstSubmitted}`,
    `**Last submitted:** ${meta.lastSubmitted}`,
    `**Reviews:** ${meta.count}/${TOTAL_REVIEWS}`,
    `**Next review date:** ${done ? "done 🎉" : meta.reviewDue}`,
    `**History:** ${meta.history.join(" → ")}`,
    "",
    `<!-- review-count: ${meta.count} -->`,
    `<!-- first-submitted: ${meta.firstSubmitted} -->`,
    `<!-- last-submitted: ${meta.lastSubmitted} -->`,
    `<!-- review-due: ${done ? "" : meta.reviewDue} -->`,
    `<!-- history: ${meta.history.join(",")} -->`,
  ];
  return lines.join("\n");
};

module.exports = ({ github, context, core }) => {
  const { owner, repo } = context.repo;

  // search for the issue whose title is exactly the problem slug (open or closed)
  const findIssue = async (slug) => {
    const result = await github.graphql(
      `query($searchQuery: String!) {
        search(query: $searchQuery, type: ISSUE, first: 20) {
          nodes {
            ... on Issue { id number title state body url }
          }
        }
      }`,
      { searchQuery: `repo:${owner}/${repo} is:issue in:title "${slug}"` },
    );
    return result.search.nodes.find((n) => n.title === slug) || null;
  };

  const createIssue = async ({ title, body }) =>
    (
      await github.graphql(
        `mutation($repoId: ID!, $title: String!, $body: String!) {
          createIssue(input: { repositoryId: $repoId, title: $title, body: $body }) {
            issue { id number url }
          }
        }`,
        { repoId: context.payload.repository.node_id, title, body },
      )
    ).createIssue.issue;

  const updateIssue = async ({ issueId, body }) =>
    github.graphql(
      `mutation($issueId: ID!, $body: String!) {
        updateIssue(input: { id: $issueId, body: $body }) { issue { id } }
      }`,
      { issueId, body },
    );

  const closeIssue = async ({ issueId }) =>
    github.graphql(
      `mutation($issueId: ID!) {
        closeIssue(input: { issueId: $issueId }) { issue { id state } }
      }`,
      { issueId },
    );

  // resolve the project id, Status field id and column option ids once per run
  let project = null;
  const getProject = async () => {
    if (project) return project;
    const result = await github.graphql(
      `query($login: String!, $number: Int!, $fieldName: String!) {
        user(login: $login) {
          projectV2(number: $number) {
            id
            title
            field(name: $fieldName) {
              ... on ProjectV2SingleSelectField { id options { id name } }
            }
          }
        }
      }`,
      { login: owner, number: PROJECT_NUMBER, fieldName: STATUS_FIELD },
    );
    const p = result.user.projectV2;
    if (!p || p.title !== PROJECT_TITLE) {
      throw new Error(`Project #${PROJECT_NUMBER} is "${p && p.title}", expected "${PROJECT_TITLE}"`);
    }
    if (!p.field) throw new Error(`Project "${PROJECT_TITLE}" has no "${STATUS_FIELD}" field`);
    project = {
      id: p.id,
      fieldId: p.field.id,
      options: Object.fromEntries(p.field.options.map((o) => [o.name, o.id])),
    };
    for (const stage of [...STAGES, DONE, DUE]) {
      if (!project.options[stage.name]) {
        throw new Error(`"${STATUS_FIELD}" has no "${stage.name}" option in "${PROJECT_TITLE}"`);
      }
    }
    return project;
  };

  // put the issue on the board (addProjectV2ItemById is idempotent) and move it to the given column
  const setStage = async (contentId, stage) => {
    const { id: projectId, fieldId, options } = await getProject();
    const added = await github.graphql(
      `mutation($projectId: ID!, $contentId: ID!) {
        addProjectV2ItemById(input: { projectId: $projectId, contentId: $contentId }) {
          item { id }
        }
      }`,
      { projectId, contentId },
    );
    await github.graphql(
      `mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
        updateProjectV2ItemFieldValue(input: {
          projectId: $projectId
          itemId: $itemId
          fieldId: $fieldId
          value: { singleSelectOptionId: $optionId }
        }) { projectV2Item { id } }
      }`,
      { projectId, itemId: added.addProjectV2ItemById.item.id, fieldId, optionId: options[stage.name] },
    );
  };

  const addDueLabel = (issueNumber) =>
    github.rest.issues.addLabels({ owner, repo, issue_number: issueNumber, labels: [DUE.name] });

  const removeDueLabel = async (issueNumber) => {
    try {
      await github.rest.issues.removeLabel({ owner, repo, issue_number: issueNumber, name: DUE.name });
    } catch (e) {
      if (e.status !== 404) throw e; // label wasn't on the issue
    }
  };

  // called once per problem touched by a push
  const recordSubmission = async (slug) => {
    const date = today();
    const issue = await findIssue(slug);

    if (!issue) {
      const meta = {
        count: 1,
        firstSubmitted: date,
        lastSubmitted: date,
        reviewDue: addDays(date, STAGES[0].days),
        history: [date],
      };
      const created = await createIssue({ title: slug, body: renderBody(slug, meta) });
      await setStage(created.id, STAGES[0]);
      core.info(`${slug}: created #${created.number} -> ${STAGES[0].name}, review on ${meta.reviewDue}`);
      return;
    }

    const meta = parseMeta(issue.body);

    if (issue.state === "CLOSED" || meta.count >= TOTAL_REVIEWS) {
      core.info(`${slug}: #${issue.number} already done, skipping`);
      return;
    }

    if (meta.reviewDue && date < meta.reviewDue) {
      core.info(`${slug}: #${issue.number} not due until ${meta.reviewDue}, ignoring early submit`);
      return;
    }

    meta.count += 1;
    meta.firstSubmitted = meta.firstSubmitted || date;
    meta.lastSubmitted = date;
    meta.history.push(date);

    if (meta.count >= TOTAL_REVIEWS) {
      meta.reviewDue = null;
      await updateIssue({ issueId: issue.id, body: renderBody(slug, meta) });
      await setStage(issue.id, DONE);
      await removeDueLabel(issue.number);
      await closeIssue({ issueId: issue.id });
      core.info(`${slug}: #${issue.number} -> ${DONE.name}, closed`);
      return;
    }

    const stage = STAGES[meta.count - 1];
    meta.reviewDue = addDays(date, stage.days);
    await updateIssue({ issueId: issue.id, body: renderBody(slug, meta) });
    await setStage(issue.id, stage);
    await removeDueLabel(issue.number);
    core.info(`${slug}: #${issue.number} -> ${stage.name} (${meta.count}/${TOTAL_REVIEWS}), review on ${meta.reviewDue}`);
  };

  // called daily: move every issue whose review date has arrived to status:due
  const flagDueReviews = async () => {
    const date = today();
    const issues = await github.paginate(github.rest.issues.listForRepo, {
      owner,
      repo,
      state: "open",
      per_page: 100,
    });

    for (const issue of issues) {
      if (issue.pull_request) continue;
      const { reviewDue } = parseMeta(issue.body);
      if (!reviewDue || reviewDue > date) continue;

      await setStage(issue.node_id, DUE);
      const labelled = issue.labels.some((l) => (typeof l === "string" ? l : l.name) === DUE.name);
      if (!labelled) await addDueLabel(issue.number);
      core.info(`${issue.title}: #${issue.number} due (${reviewDue}) -> ${DUE.name}`);
    }
  };

  return { recordSubmission, flagDueReviews };
};

module.exports.parseMeta = parseMeta;
module.exports.renderBody = renderBody;
module.exports.addDays = addDays;
module.exports.today = today;
