class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        hashMap = {
        "}": "{",
        "]": "[",
        ")": "("
        }


        for i in s:

            if len(stack) > 0  and  i in hashMap:

                if stack[-1] == hashMap[i]: 
                    stack.pop()
                    continue
                else: return False

            stack.append(i)

        return len(stack) == 0