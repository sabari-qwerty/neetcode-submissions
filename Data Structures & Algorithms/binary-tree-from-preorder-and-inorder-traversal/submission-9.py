# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorderIdx, inorderIdx = 0, 0 

        def helper(limit):

            nonlocal preorderIdx
            nonlocal inorderIdx


            if preorderIdx >= len(preorder):
                return None

            if inorder[inorderIdx] == limit: 
                inorderIdx += 1
                return None 
            
            root = TreeNode(preorder[preorderIdx])
            preorderIdx += 1
            root.left = helper(root.val)
            root.right = helper(limit)

            return root

        return helper(float('inf'))

