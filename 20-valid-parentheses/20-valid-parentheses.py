class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dc = {'(':')', '[':']', '{':"}"}
        
        for c in s:
            last = stack[-1] if stack else ''
            
            if last in dc and dc[last] == c:
                stack.pop()
            
            else:
                stack.append(c)
        
        return not stack
                
            