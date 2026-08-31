class Solution:
    def isValid(self, s: str) -> bool:
        stack, states = [], {'}': '{', ']': '[', ')': '('}
        for curr in s: 
            if curr in states: 
                if stack and stack[-1] == states[curr]: 
                    stack.pop()
                
                else: return False 

            else: stack.append(curr)

        return True if not stack else False 