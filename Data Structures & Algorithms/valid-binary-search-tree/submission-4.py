# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        q  = deque([(root, float('-inf'), float('inf'))])


        while q:

            mid, left, right = q.popleft()

            if not (left < mid.val < right): 
                return False
            if mid.left:
                q.append((mid.left, left, mid.val))
            if mid.right:
                q.append((mid.right, mid.val, right))
        
        return True

        