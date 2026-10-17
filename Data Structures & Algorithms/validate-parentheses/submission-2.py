class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {
            "}": "{",
            "]": "[",
            ")": "(" 
        }

        stack = []

        for i in s:
            print(stack)

            if i in hashMap: 

                if not len(stack) or hashMap[i] != stack[-1]: return False

                stack.pop()
                continue

            stack.append(i)

        return False if len(stack) else True

