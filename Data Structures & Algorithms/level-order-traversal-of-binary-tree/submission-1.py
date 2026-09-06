# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        res = []


        def dsf(root, count=0): 
            if not root: return 
            if len(res) == count: 
                res.append([])

            res[count].append(root.val)

            dsf(root.left, count+1)
            dsf(root.right, count+1)

        dsf(root)


        return res