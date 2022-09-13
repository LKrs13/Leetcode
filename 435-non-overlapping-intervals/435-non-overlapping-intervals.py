class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Example: [[1,4],[2,3],[3,5]] 
        
        intervals.sort() 
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            
            # If don't overlap
            if start >= prevEnd:
                
                # Update end time
                prevEnd = end
            
            # If overlap
            else:
                res += 1
                
                # Erase interval with larger end time
                prevEnd = min(prevEnd, end)
        
        return res