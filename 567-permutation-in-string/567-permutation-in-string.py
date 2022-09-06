class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        k = len(s1)

        window = s2[:k]
        d2 = Counter(window)

        if d1 == d2:
            return True

        for i in range(len(s2)-k):

            d2[s2[i]] -= 1
            d2[s2[i+k]] += 1   

            if d1 == d2:
                return True
            
        return False