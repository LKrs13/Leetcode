class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        visited = set()
        
        while l <= r and r < len(s):
            if s[r] in visited:
                l += 1
                r = l
                visited.clear()
            
            else:
                visited.add(s[r])
                r += 1
            
            res = max(res, r-l)
        
        return res
            
            
            