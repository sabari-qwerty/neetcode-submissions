class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_consecutive_sequence_length = 0 

        unqiue = set(nums)

        for i in unqiue: 

            if i +1 in unqiue: continue

            value = i

            count = 0 

            while value in unqiue: 

                value -= 1
                count += 1

            max_consecutive_sequence_length =max(max_consecutive_sequence_length, count)

        return max_consecutive_sequence_length

                