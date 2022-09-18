class Solution:
    
    def generateParenthesis(self, n):
        if not n:
            return []
        
        res = []
        def dfs(left, right, string):
            if right < left:
                return
            
            if not left and not right:
                res.append(string)
                return
            
            if left:
                dfs(left-1, right, string + "(")
                
            if right:
                dfs(left, right-1, string + ")")
            
        dfs(n, n, "")
        
        return res
