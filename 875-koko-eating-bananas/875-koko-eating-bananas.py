class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        l, r = 1, mx
        
        while l < r:
            k = (l + r) // 2
            pilesCopy = [x for x in piles]
            tmp = h
            i = 0
            
            while tmp > 0 and i < len(piles):
                tmp -= ceil(pilesCopy[i] / k)
                if tmp < 0:
                    break
                pilesCopy[i] = 0
                i += 1
            
            if pilesCopy[-1] != 0:
                l = k + 1
                
            else:
                r = k
        
        return l