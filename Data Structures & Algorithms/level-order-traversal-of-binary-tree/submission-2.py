# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if not root: return result

        currq = [root]
        nextq = []

        while currq or nextq:

            level = []

            for q in currq: 

                level.append(q.val)

                if q.left: 
                    nextq.append(q.left)
                if q.right: 
                    nextq.append(q.right)

            currq = nextq
            nextq = []

            if level: 
                result.append(level)

        return result

    


