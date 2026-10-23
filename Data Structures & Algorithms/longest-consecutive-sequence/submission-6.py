class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        most_logest_consecutive_length = 0 

        nums = set(nums)

        for r in nums: 

            if r + 1 in nums: continue

            print(r)

            findedValue = r -1

            count = 1

            while findedValue in nums:

                count += 1 
                
                findedValue -= 1

            most_logest_consecutive_length = max(most_logest_consecutive_length, count)

        return most_logest_consecutive_length