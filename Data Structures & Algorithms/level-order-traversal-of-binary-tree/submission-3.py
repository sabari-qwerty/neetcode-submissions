# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        curr = [root]
        next_ = []

        while curr:

            level = []

            for tree in curr:
                if not tree: continue  

                level.append(tree.val)
                if tree.left: next_.append(tree.left)
                if tree.right: next_.append(tree.right)

            if level: 
                ans.append(level)
            
            curr = next_
            next_ = []

        return ans

         