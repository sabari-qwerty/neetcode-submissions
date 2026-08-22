class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        window = set()

        count = 0

        maxLen = 0

        for i in s: 

            while i in window:

                window.remove(s[count])

                count += 1

            window.add(i)

            maxLen = max(maxLen, len(window))

        return maxLen