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
                a, b = stack.pop(), stack.pop()
                res = dc[c](b, a)
                stack.append(res)
                
            else:
                stack.append(int(c))
        
        return stack[0]