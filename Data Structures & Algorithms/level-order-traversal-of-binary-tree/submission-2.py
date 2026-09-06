# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        q = collections.deque()
        q.append(root)

        while q: 
            qLen = len(q)
            level = []
            for i in range(qLen):
                first_value = q.popleft()
                if first_value:
                    level.append(first_value.val)
                    q.append(first_value.left)
                    q.append(first_value.right)

            if level:
                ans.append(level)


        return ans
        