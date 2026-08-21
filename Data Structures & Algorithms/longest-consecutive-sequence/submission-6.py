class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        set_nums = set(nums)

        n = len(nums)

        ans = 0 

        for i in nums: 

            if i + 1 in set_nums: continue

            count = 0 

            j = i 

            while j in set_nums: 

                count += 1

                j -= 1

            ans = max(ans, count)

        return ans

        