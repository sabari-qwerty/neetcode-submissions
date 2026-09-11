class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        closing_tag_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:

            if i not in closing_tag_map: 
                stack.append(i)
            elif len(stack) and i in closing_tag_map and   stack[-1] == closing_tag_map[i]: 
                stack.pop()
            else: 
                return False

        return len(stack) == 0 
