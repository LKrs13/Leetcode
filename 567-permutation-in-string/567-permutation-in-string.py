class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # moves window of len(s1) one char at a time and
        # updates counter by removing first letter and adding last letter
        # to have current window char frequency
        
        d1 = Counter(s1)
        k = len(s1)

        window = s2[:k]
        d2 = Counter(window)

        if d1 == d2:
            return True

        for i in range(len(s2)-k):
            print(s2[i], s2[i+k])
            print(d2)
            d2[s2[i]] -= 1
            d2[s2[i+k]] += 1   

            if d1 == d2:
                return True
            
        return False