class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()

        n = len(s)

        count = 0 

        maxValue = 0 

        for i in range(n):

            while s[i] in window:

                window.remove(s[count]) 

                count +=1
            
            window.add(s[i])
            maxValue = max(maxValue, len(window))



        return maxValue





