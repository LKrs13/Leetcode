class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dc =  {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        stack = []
        
        for c in tokens:
            if c in dc and len(stack) > 1:
                a = stack.pop()
                res = dc[c](stack[-1], a)
                stack[-1] = res
                
            else:
                stack.append(int(c))
        
        return stack[0]