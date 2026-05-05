class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack, operations = [], ['+', '-', '/', '*']
        for value in tokens:

            if value in operations: 
                b = stack.pop()
                a = stack.pop()
                if value == '+': stack.append(a + b)
                elif value == '-': stack.append(a - b)
                elif value == '*': stack.append(a * b)
                else: stack.append(int(a / b))
            else: 
                stack.append(int(value))
        
        return int(stack.pop())