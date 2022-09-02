class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        "aacd", "erdsgacadbsr"
        
        ct = Counter(s1)
        
        for i in range(len(s2)):
            if s2[i] in ct:
                dc = Counter(s2[i:i+len(s1)])
                if dc == ct:
                    return True
        
        return False