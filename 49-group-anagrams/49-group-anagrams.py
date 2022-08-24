class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dc = {}
        
        for n in strs:
            x = "".join(sorted(n))
            
            if x in dc:
                dc[x].append(n)
            
            else:
                dc[x] = [n]
        
        return dc.values()