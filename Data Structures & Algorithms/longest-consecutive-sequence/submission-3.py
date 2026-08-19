class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        set_num = set(nums)


        ans = 0 
        for i in nums: 

            if i + 1 in set_num: continue

            j = i 

            count = 0 

            while j in set_num: 

                j -=1
                count += 1


            ans = max(ans, count)

        return ans

            