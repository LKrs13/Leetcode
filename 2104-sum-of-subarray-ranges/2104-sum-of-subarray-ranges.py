class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ct = 0
        
        for i in range(len(nums)):
            curMin, curMax = nums[i], nums[i]
            
            for j in range(i + 1, len(nums)):
                curMin, curMax = min(curMin, nums[j]), max(curMax, nums[j])
                ct += (curMax - curMin)
        
        return ct