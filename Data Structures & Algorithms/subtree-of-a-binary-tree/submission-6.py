# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def serlinzation(self, s): 

        res = []


        def dfs(s): 

            if not s: 
                res.append('$#')
                return 

            res.append("$")
            res.append(str(s.val))
            dfs(s.right)
            dfs(s.left)

        dfs(s)

        return "".join(res)

    
    def z_funation(self, s):
        n = len(s) 
        z_array = [0] * n  

        l, r = 0, 0

        for k in range(1, n): 

            if r < k: 
                l, r = k, k

                while r < n and s[r] == s[r - l]: 
                    r += 1

                z_array[k] = r - l 
                r -= 1

            else: 

                k1 = k - l 

                if z_array[k1] < r - k +1:
                    z_array[k] = z_array[k1]

                else: 

                    l = k 

                    while r < n and s[r] == s[r-l]: 
                        r += 1

                    z_array[k] = r - l 
                    r -= 1

                    

        return z_array

    



    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        root_serlinzation =  self.serlinzation(root)
        subRoot_serlinzation = self.serlinzation(subRoot)

        compnaine = subRoot_serlinzation + "|" + root_serlinzation

        z_arry = self.z_funation(compnaine)

        for i in z_arry: 

            if i == len(subRoot_serlinzation): return True



        return False 

        