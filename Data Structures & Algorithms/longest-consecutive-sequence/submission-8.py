class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        freq = {}

        for i in nums: 

            freq[i] = freq.get(i, 0) + 1

        ans = 0 

        for i in freq:

            if i +1 in freq: continue

            maxVlaue = i 
            maxConsecutiveSequence = 0 

            while maxVlaue in freq:

                maxVlaue -= 1
                maxConsecutiveSequence += 1

            ans = max(maxConsecutiveSequence, ans)

        return ans

