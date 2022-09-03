class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # [1,2,3,4,5] 1
        # [2,3,4,5,1] 2
        # [3,4,5,1,2] 2
        # [4,5,1,2,3] 1
        # [5,1,2,3,1] 2
        # want to look at side that is not sorted
        # since we are guaranteed to find a bigger number 
        # in the sorted side
        
        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l + r) // 2
            
            # right side is sorted (increasing) => want to look left to find smaller
            if nums[m] < nums[r]:
                r = m
            
            else:
                l = m + 1
            
        return nums[l]
    