class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)

        ans = set()

        sorted_list =  sorted(nums)
        for i in range(n): 

            l = i + 1
            r = n -1

            while l < r: 

                Sum = sorted_list[i] + sorted_list[l] + sorted_list[r]

                if Sum > 0: 
                    r -= 1
                elif Sum < 0: 
                    l += 1

                else: 
    
                    ans.add((sorted_list[i], sorted_list[l], sorted_list[r]))
                    l += 1
                    while sorted_list[l] == sorted_list[r] and l < r: l += 1 


        return [list(i) for i in ans]

