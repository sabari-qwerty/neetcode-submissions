# LeetCode Review Cycle — spaced-repetition automation

This repo is filled automatically by [NeetCode GitHub Sync](https://neetcode.io/profile/github).
On top of that, two GitHub Actions workflows turn every problem you solve into a **GitHub issue** and move it
across a **GitHub Project board** on a spaced-repetition schedule. A problem stays in rotation until you have
solved it 5 times at the right intervals.

---

## 1. The review cycle

| Review | When                      | What you do                  | Card moves to  | Next review        |
|--------|---------------------------|------------------------------|----------------|--------------------|
| 1      | First time you submit     | Learn and solve              | `stage:day3`   | +3 days            |
| 2      | On/after review date      | Struggle, learn and solve    | `stage:day5`   | +5 days            |
| 3      | On/after review date      | Struggle and solve           | `stage:day7`   | +7 days            |
| 4      | On/after review date      | Struggle and solve           | `stage:day30`  | +30 days           |
| 5      | On/after review date      | Struggle and solve           | `stage:done`   | — issue is closed  |

Rules:

- The next review date counts from the **last** submit, not the first one.
- When a review date arrives, the daily job moves the card to **`status:due`** (and adds a `status:due` label).
- A submit **before** the review date is ignored. Extra practice is fine, but it doesn't skip stages.
- After review 5 the issue is closed. Later submits of that problem are ignored.

Example for a problem first solved on 2026-09-28:

```
09-28  submit #1  -> stage:day3   (due 10-01)
10-01  3 AM job   -> status:due
10-01  submit #2  -> stage:day5   (due 10-06)
10-06  3 AM job   -> status:due
10-06  submit #3  -> stage:day7   (due 10-13)
10-13  3 AM job   -> status:due
10-13  submit #4  -> stage:day30  (due 11-12)
11-12  3 AM job   -> status:due
11-12  submit #5  -> stage:done, issue closed
```

---

## 2. How it works

```
 NeetCode submit
      │  (GitHub Sync pushes  "Data Structures & Algorithms/<slug>/submission-N.py")
      ▼
 ┌────────────────────────────────┐        ┌──────────────────────────────────┐
 │ Track Submission Progress      │        │ Flag Due Reviews                 │
 │ .github/workflows/main.yml     │        │ .github/workflows/schedule.yml   │
 │ trigger: push to main          │        │ trigger: daily 03:00 IST + manual│
 └───────────────┬────────────────┘        └────────────────┬─────────────────┘
                 │ recordSubmission(slug)                   │ flagDueReviews()
                 ▼                                          ▼
          ┌──────────────────────────────────────────────────────────┐
          │ .github/scripts/review-cycle.js  (shared logic)          │
          └───────┬──────────────────────────────────┬───────────────┘
                  ▼                                  ▼
         Issue per problem                   Project board "LeetCode Review Cycle"
         (title = slug, state in body)       (Status column = stage)
```

### Files

| File | Purpose |
|------|---------|
| `.github/workflows/main.yml` | Runs on every push to `main` that touches `Data Structures & Algorithms/**/submission-*.py`. Finds the changed problem folders and calls `recordSubmission` once per problem. |
| `.github/workflows/schedule.yml` | Runs every day at **03:00 IST** (`cron: '30 21 * * *'`, UTC). You can also start it by hand. Calls `flagDueReviews`. |
| `.github/scripts/review-cycle.js` | All the logic: finding the project, issue lookup/create/update/close, date math, and moving cards. |

### What happens on a submit (`recordSubmission`)

1. The problem **slug** comes from the file path (`Data Structures & Algorithms/two-sum/submission-3.py` → `two-sum`).
   NeetCode's `submission-N` number is **not** used, because it counts every NeetCode submit, not reviews.
2. The script searches for an issue whose title is **exactly** the slug, open or closed.
3. Then:
   - **No issue:** creates it with review 1 and moves the card to `stage:day3`. The due date is today + 3.
   - **Closed, or 5 reviews already:** skips it.
   - **Not due yet** (today < review date): logs `ignoring early submit` and changes nothing.
   - **Due:** adds one to the review count, sets the next stage and due date, updates the issue text, and removes the `status:due` label.
     On review 5 it moves the card to `stage:done` and closes the issue.

### What happens every morning (`flagDueReviews`)

For every **open** issue whose `review-due` date is today or earlier, the job moves the card to `status:due` and adds the `status:due` label.

### Where the state is kept

There is no database. Each issue's text holds its state in hidden HTML comments:

```
**Problem:** two-sum
**Neetcode URL:** https://neetcode.io/problems/two-sum/question
**First submitted:** 2026-09-28
**Last submitted:** 2026-10-01
**Reviews:** 2/5
**Next review date:** 2026-10-06
**History:** 2026-09-28 → 2026-10-01

<!-- review-count: 2 -->
<!-- first-submitted: 2026-09-28 -->
<!-- last-submitted: 2026-10-01 -->
<!-- review-due: 2026-10-06 -->
<!-- history: 2026-09-28,2026-10-01 -->
```

The visible lines are for you to read. The workflows only read the `<!-- ... -->` lines.
You can edit those lines by hand (Issue → ⋯ → Edit) to change a problem's state, for example to make it due today while testing.

### How the right board is found

The script never uses hard-coded project or column IDs. On each run it:

1. Loads project **number `PROJECT_NUMBER`** of the repo owner (`github.com/users/<owner>/projects/<number>`).
2. Checks that its title is **exactly `PROJECT_TITLE`**. If not, the run fails and changes nothing, so it can't touch another project.
3. Looks up each column (`stage:day3` … `status:due`) **by name** in the project's `Status` field. If one is missing, the run fails with an error.

All dates are `YYYY-MM-DD` in **IST (UTC+5:30)**.

---

## 3. Setting it up for a new project / repo

### Step 1 — Create the project board

1. Go to **github.com → your profile → Projects → New project → Board**. Name it, e.g. `LeetCode Review Cycle`.
2. Open the **`Status`** field (⋯ on any column → *Edit field*, or project **Settings → Fields → Status**)
   and create these options. The names must match exactly:

   | Option        | Suggested description           |
   |---------------|---------------------------------|
   | `status:due`  | Review date reached, solve now  |
   | `stage:day3`  | Solved once, review in 3 days   |
   | `stage:day5`  | Review in 5 days                |
   | `stage:day7`  | Review in 7 days                |
   | `stage:day30` | Review in 30 days               |
   | `stage:done`  | Finished all 5 reviews          |

   You can delete the default options (`Todo`, `In Progress`, `Done`).
3. Note the **project number** from the URL: `github.com/users/<you>/projects/<NUMBER>`.
4. Optional: in the project's **Workflows** settings, turn **off** the built-in "Item closed → Done" and
   "Item added → Todo" workflows so they don't fight with the script.

> The script looks the project up with `user(login: <repo owner>)`, so the project has to be owned by the
> same **user account** that owns the repo. If you use an organization, change `user(login:` to
> `organization(login:` in `getProject()` in `review-cycle.js`.

### Step 2 — Create a token (`PROJECT_TOKEN`)

The default `GITHUB_TOKEN` can't edit a user-owned Project, so you need a personal access token.

**Classic token** (Settings → Developer settings → Personal access tokens → Tokens (classic)) with scopes:

- `repo`
- `project`

**Or a fine-grained token**, limited to this repository, with:

- Repository permissions: **Issues: Read and write**, **Contents: Read-only**, **Metadata: Read-only**
- Account permissions: **Projects: Read and write**

Set an expiry and remember to renew it. When the token expires, every run fails with an auth error.

### Step 3 — Add the secret to the repo

1. Repo → **Settings → Environments → New environment** → name it **`production`**.
   Both workflows use `environment: production`.
2. In that environment, click **Add environment secret**: name **`PROJECT_TOKEN`**, value = the token from Step 2.

### Step 4 — Copy the files

Copy these three files into the new repo, keeping the same paths:

```
.github/scripts/review-cycle.js
.github/workflows/main.yml
.github/workflows/schedule.yml
```

### Step 5 — Set the config

At the top of `.github/scripts/review-cycle.js`:

```js
const PROJECT_NUMBER = 6;                      // <- your project number from Step 1
const PROJECT_TITLE = "LeetCode Review Cycle"; // <- your project's exact title
const STATUS_FIELD = "Status";                 // field holding the columns

const STAGES = [                               // review gaps; names must exist in Status
  { name: "stage:day3", days: 3 },
  { name: "stage:day5", days: 5 },
  { name: "stage:day7", days: 7 },
  { name: "stage:day30", days: 30 },
];
const DONE = { name: "stage:done" };
const DUE = { name: "status:due" };

const IST_OFFSET_MS = 5.5 * 60 * 60 * 1000;    // your timezone offset from UTC
```

Other settings you may want to change:

- **Problem folder / language:** `main.yml` only watches `Data Structures & Algorithms/**/submission-*.py`.
  Change the `paths:` filter **and** the `git diff ... --` pattern in the same file to add other topics or languages
  (for example `'**/submission-*.*'`).
- **Run time:** the `cron` in `schedule.yml` is in **UTC**. 03:00 IST = `30 21 * * *`.
  Use [crontab.guru](https://crontab.guru) to convert your local time.
- **More or fewer reviews:** add or remove items in `STAGES` and create matching options in the `Status` field.
  The total number of reviews is always `STAGES.length + 1`.

### Step 6 — Connect NeetCode

On [neetcode.io/profile/github](https://neetcode.io/profile/github), connect GitHub, pick this repo, and turn on **Auto-commit**.
Choose "accepted only" if failed attempts shouldn't count as reviews.

### Step 7 — Test it

1. Submit any problem on NeetCode.
2. Repo → **Actions → Track Submission Progress**, then open the latest run. The log should show:
   `<slug>: created #N -> stage:day3, review on YYYY-MM-DD`
3. Check that the issue exists and its card is in `stage:day3` on the board.
4. Edit the issue and change `<!-- review-due: ... -->` to today's date.
5. **Actions → Flag Due Reviews → Run workflow.** The card should move to `status:due`.
6. Submit the same problem again. The card should move to `stage:day5` and the issue should show `Reviews: 2/5`.

---

## 4. Troubleshooting

Check the log first: **Actions →** open the run **→ track-progress / flag-due → "Update issue per problem" /
"Move due reviews to status:due"**.

| Log message / symptom | Cause | Fix |
|---|---|---|
| `not due until YYYY-MM-DD, ignoring early submit` | Submitted before the review date. | Expected. Submit again on or after that date. |
| `already done, skipping` | The issue is closed or has 5 reviews. | Expected. Reopen and edit `review-count` to go through it again. |
| `Project #N is "X", expected "Y"` | `PROJECT_NUMBER` points to a different project. | Fix `PROJECT_NUMBER` / `PROJECT_TITLE`. |
| `"Status" has no "stage:dayX" option` | A column name doesn't match exactly. | Rename the option on the board, or fix `STAGES`. |
| `has no "Status" field` | The field is named differently. | Fix `STATUS_FIELD`. |
| `Resource not accessible` / `INSUFFICIENT_SCOPES` / `Bad credentials` | The token is missing, expired, or lacks project permission. | Recreate the token (Step 2) and update the secret (Step 3). |
| The workflow didn't run at all | The changed file isn't matched by the `paths:` filter, or the push wasn't to `main`. | Check the `paths:` in `main.yml`. |
| The 3 AM job ran late | GitHub delays scheduled runs when it's busy. | Normal, usually under an hour. Run it by hand if needed. |
| Scheduled runs stopped | GitHub turns off schedules after 60 days with no repo activity. | Push any commit or re-enable it in Actions. |
| Two issues for one problem | An old issue had a different title or no hidden state. | Close the extra issue. The script matches the exact title only. |

---

## 5. Manual controls

| Want to… | Do this |
|---|---|
| Run the due check now | Actions → **Flag Due Reviews** → Run workflow |
| Make a problem due today | Edit the issue → set `<!-- review-due: <today> -->` |
| Restart a problem from scratch | Reopen the issue, then edit it: set `review-count: 0` and clear `review-due` (`<!-- review-due:  -->`). The next submit puts it back at `stage:day3`. Deleting the issue works too: the next submit creates a new one. |
| Skip a problem forever | Close its issue |
