# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root, count=0): 

            if not root: return count

            return max(helper(root.left, count+1), helper(root.right, count+1) ) 

        return helper(root)