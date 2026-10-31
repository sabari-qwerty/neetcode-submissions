# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        hashMap = {}

        ans = []

        def helper(root, count=0):


            if not root: return 

            if count in hashMap: 
                hashMap[count].append(root.val)
            else: 
                hashMap[count] = [root.val]

            helper(root.left, count+1)
            helper(root.right, count+1)

        helper(root)
        
        for i in hashMap: 

            ans.append(hashMap[i])


        return ans

