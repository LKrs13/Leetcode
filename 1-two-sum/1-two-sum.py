class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        dc = {}
        
        for i, n in enumerate(nums):
            if n in dc:
                return [i, dc[n]]
            
            rest = target - n
            dc[rest] = i
            
            