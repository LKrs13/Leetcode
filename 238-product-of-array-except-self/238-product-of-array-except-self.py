class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Calculer le produit des numéros à gauche avec les numéros
        # à droite de chaque index 
        
        # [1, 1, 2, 6]
        # [24, 12, 4, 1]
        
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
    