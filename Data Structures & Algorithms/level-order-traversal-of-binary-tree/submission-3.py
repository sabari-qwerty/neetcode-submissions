# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        if not root: return res

        q = [root]

        while q: 
            current = []
            level = []
            n = len(q)

            for i in range(n):

                node = q[i]

                if node:

                    level.append(node.val)
                    current.append(node.left)
                    current.append(node.right)

            if level: 
                res.append(level)

            q = current

        return res