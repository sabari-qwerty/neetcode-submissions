# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(low, mid, high):

            if not mid: return True

            if low >= mid.val or mid.val >= high:
                return False

            return check(low, mid.left, mid.val) and check(mid.val, mid.right, high)

        return check(float('-inf'), root, float('inf'))