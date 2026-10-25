class Solution:
    def isValid(self, s: str) -> bool:
        

        hashMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for i in s:

            if i in hashMap: 

                if len(stack)> 0 and i in hashMap:

                    if hashMap[i] != stack[-1]: return False

                    stack.pop()
                else: 
                    return False

            else: 
                stack.append(i)


        return len(stack) == 0

