class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0

        while l < r:
            m = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += ceil(p / m)
                
            if totalTime <= h:
                r = m
                
            else:
                l = m + 1
        
        return l