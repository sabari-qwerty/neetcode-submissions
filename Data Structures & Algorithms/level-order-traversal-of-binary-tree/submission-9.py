# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        current = [root]
        next_ = []

        while current: 

            level = []

            for c in current: 

                if not c: continue


                level.append(c.val)
                if c.left: 
                    next_.append(c.left)
                if c.right:
                    next_.append(c.right)

            if not level: break

            ans.append(level)
            current = next_
            next_ = []

        return ans

