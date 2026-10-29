# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def sameTree(self, p1, p2): 

        if not p1 and not p2: return True

        if not p1 and p2: return False 
        if p1 and not p2: return False

        if p1.val != p2.val: return False

        left = self.sameTree(p1.left, p2.left)
        right = self.sameTree(p1.right, p2.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        print("i am in")

        if not root: return False

        print(root.val, subRoot.val)

        if root.val == subRoot.val: 


            if self.sameTree(root, subRoot): return True

        left =  self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right 

