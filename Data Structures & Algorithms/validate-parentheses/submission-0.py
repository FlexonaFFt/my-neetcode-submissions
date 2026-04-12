class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        opening = set(pairs.values())
        stack, status = [], False 

        for element in s:
            if element in opening: 
                stack.append(element)
            elif element in pairs:
                if not stack:
                    return False 
                current_top = stack.pop()
                if current_top != pairs[element]:
                    return False 
        if not stack: return True
        else: return False 