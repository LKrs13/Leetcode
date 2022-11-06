import heapq 

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []
        dc = {}
        
        for student, score in items:
            if student not in dc:
                dc[student] = []
                heapq.heapify(dc[student])
                
            heapq.heappush(dc[student], score)
            
            while len(dc[student]) > 5:
                heapq.heappop(dc[student])
        
        for student, scores in dc.items():
            res.append([student, sum(scores) // 5])
        
        return sorted(res)
    
    
    