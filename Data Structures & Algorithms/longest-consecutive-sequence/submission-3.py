class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)


        max_count = 0 

        for i in nums_set:

            if i + 1 in nums_set: continue

            count = 1

            val = i - 1

            while val  in nums_set: 

                val -= 1

                count += 1

            max_count = max(count, max_count)


        return max_count
    