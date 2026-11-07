# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans = []

        def iter(root):

            if not root: return 

            iter(root.left)
            ans.append(root.val)
            iter(root.right)

        iter(root)
        return ans[k-1]