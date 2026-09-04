# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True
        if not root: return False

        if self.checkSameTree(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot) 


    def checkSameTree(self, r, s):

        if not r and not s: return True 
        if r and not s: return False

        if (r and s) and r.val == s.val: 
            return (self.checkSameTree(r.right, s.right) and
            self.checkSameTree(r.left, s.left))

        return False

