class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {
            "]": "[", 
            ")": "(",
            "}": "{"
        }

        stack = []

        for char in s: 

            if char in hashMap:
                if not len(stack): return False 
                if len(stack) and stack[-1] != hashMap[char]: return False
                stack.pop()

            else: 
                stack.append(char)

        return len(stack) == 0 