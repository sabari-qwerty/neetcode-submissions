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

        while curr or next_:

            level = []

            for i in curr: 

                if not i: continue

                level.append(i.val)

                next_.append(i.left)
                next_.append(i.right)

            if not level: break

            ans.append(level)
            curr = next_
            next_ = []


        return ans