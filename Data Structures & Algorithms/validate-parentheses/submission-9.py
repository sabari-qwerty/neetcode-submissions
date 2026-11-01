class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        hashMap = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for i in s: 

            if i in hashMap:
                if not stack: return False
                
                if hashMap[i] != stack.pop(): return False

                continue

            stack.append(i) 


        print(stack)
        return not stack 