class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hashMap = {
            "}": "{",
            ")": "(",
            "]":"["
        }

        for i in s:

            if i in hashMap: 

                if len(stack) and hashMap[i] == stack[-1]:
                    stack.pop() 
                else:     
                    return False

            else: 
                stack.append(i)

        return len(stack) == 0



