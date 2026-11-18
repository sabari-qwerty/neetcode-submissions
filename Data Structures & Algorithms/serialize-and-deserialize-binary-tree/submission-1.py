# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        ans = []

        def dfs(node):

            if not node: 

                ans.append('N')
                return None

            ans.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        return ",".join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        res = data.split(',')

        self.idx = 0

        print(res)

        def dfs():

            if res[self.idx] == "N": 
                self.idx += 1
                return None 

            root = TreeNode(int(res[self.idx]))
            self.idx += 1

            root.left = dfs()
            root.right = dfs()

            return root 

        return  dfs()






