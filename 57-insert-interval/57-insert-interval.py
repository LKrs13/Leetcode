class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            newStart, newEnd = newInterval

            # check if new interval goes before cur interval (don't overlap)
            if newEnd < start:
                
                # if so, just return new interval with the rest after
                res.append(newInterval)
                return res + intervals[i:]
            
            # check if new interval goes after cur interval (don't overlap)
            elif newStart > end:
                
                # if so, just add cur interval
                res.append(intervals[i])
                
            # if new interval and cur interval overlap
            else:
                # update new interval by merging 
                newInterval = [min(newStart, start), max(newEnd, end)]
        
        # if new interval never went before cur one, add it to the end
        res.append(newInterval)
        return res