class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dc = {}
        
        for n in nums:
            dc[n] = float(inf)
            
            if n+1 in dc:
                dc[n] = (n+1)
            
            if n-1 in dc:
                dc[n-1] = (n)
        
        for i, j in dc.items():
            
            if i-1 in dc:
                continue
                
            tmp = j
            ct = 1
            
            while tmp in dc and tmp != float('inf'):
                ct += 1
                tmp = dc[tmp]
                
            res = max(res, ct)
        
        return res