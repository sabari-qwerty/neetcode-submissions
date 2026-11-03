# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = set()

        def check(node):

            if not node: return node

            check(node.left)
            if node: ans.add(node.val)

            check(node.right)
            if node: ans.add(node.val)

        check(root)

        return list(ans)[k-1]




 

        