class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        timeVals = self.timeMap[key]
        
        l, r = 0, len(timeVals)-1
        while l < r:
            m = (l + r + 1) // 2
            
            if timeVals[m][0] > timestamp:
                r = m - 1
                
            else:
                l = m
        
        return timeVals[l][1] if timeVals[l][0] <= timestamp else ""
            
        
        

'''
[1 - 4]
2
{
    foo: [[2:bar], [4:bar2], [5:bar3], [6:bar4], [7:bar5]]
},
{
    foo: [1, 4, 5]
}
'''