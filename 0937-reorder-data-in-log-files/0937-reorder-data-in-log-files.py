class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        '''
        ["a1 9 2 3 1","g1 act car", "ab1 off key dog", "a8 act zoo","a2 act car"]
        '''
        
        res = []
        letterLogs = []
        digitLogs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digitLogs.append(log)
            
            else:
                letterLogs.append(log)
        
        letterLogs = sorted(letterLogs, key = lambda x: (x.split()[1:], x.split()[0]))
        
        res += (letterLogs)
        res += (digitLogs)
        
        return res