class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)

        n = len(nums)

        ans = 0 


        for i in hash_set:

            if i + 1 in  hash_set: continue

            val = i 
            count = 0 

            while val in hash_set: 

                val -= 1

                count += 1

            ans = max(ans, count)

        return ans