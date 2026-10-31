class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        hashMap = {}

        l = 0 
        n = len(s)

        maxFreq = 0 
        ans = 0 

        for r in range(n):

            key = s[r]

            hashMap[key] = hashMap.get(key, 0) + 1

            maxFreq = max(maxFreq, hashMap[key])

            while (r - l + 1) -  maxFreq > k:

                key = s[l]

                hashMap[key] -= 1

                l += 1

            ans = max(ans, r - l +1)

        return ans

 