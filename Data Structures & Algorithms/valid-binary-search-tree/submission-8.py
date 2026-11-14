# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(low, mid, right):

            if not mid: return True

            if not low < mid.val < right:

                return False

            return helper(low, mid.left, mid.val) and helper(mid.val, mid.right, right)

        return helper(float('-inf'), root, float('inf'))