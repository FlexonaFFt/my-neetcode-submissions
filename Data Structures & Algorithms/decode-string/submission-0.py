class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']': 
                stack.append(s[i])
            else: 
                helper = ""
                while stack[-1] != '[': helper = stack.pop() + helper
                stack.pop()

                curr = ""
                while stack and stack[-1].isdigit():
                    curr = stack.pop() + curr
                stack.append(int(curr) * helper)
            
        return "".join(stack)