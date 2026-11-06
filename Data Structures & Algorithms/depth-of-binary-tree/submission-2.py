# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root, maxDepth=0):

            if not root: return maxDepth

            return max(helper(root.left, maxDepth+1), helper(root.right, maxDepth+1) )

        return helper(root)

