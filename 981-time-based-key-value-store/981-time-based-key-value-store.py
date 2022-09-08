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
        
        res = ""
        timeVals = self.timeMap[key]
        
        l, r = 0, len(timeVals)-1
        while l <= r:
            m = (l + r) // 2
            
            if timeVals[m][0] <= timestamp:
                res = timeVals[m][1]
                l = m + 1
            
            else:
                r = m - 1
        
        return res
            
        
        

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