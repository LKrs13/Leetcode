class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        num1 = nums[1:]
        num2 = nums[0:n - 1]
        
        memo1 = {}
        memo2 = {}
        
        def dfs(i, nums, memo):
            if i in memo:
                return memo[i]
            
            if not (0 <= i < len(nums)):
                return 0
            
            # On peut décider d'inclure le num présent ou de passer au prochain
            incl = nums[i] + dfs(i + 2, nums, memo)
            excl = 0 + dfs(i + 1, nums, memo)
            
            memo[i] = max(incl, excl)
            
            return memo[i]
        
        if n != 1:
            return max(dfs(0, num1, memo1), dfs(0, num2, memo2))
        else:
            return dfs(0, nums, memo1)
            