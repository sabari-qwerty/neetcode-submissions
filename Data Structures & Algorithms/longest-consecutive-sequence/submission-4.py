class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)

        maxCount = 0 

        for i in unique:

            if i + 1 in unique: continue 

            data = i 

            count = 0 

            while data in unique: 

                data -= 1
                count += 1

            maxCount = max(maxCount, count)

        return maxCount