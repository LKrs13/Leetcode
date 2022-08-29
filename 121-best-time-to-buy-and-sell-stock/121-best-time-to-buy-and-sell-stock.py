class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 0
        
        while l <= r and r < len(prices):
            if prices[r] < prices[l]:
                l = r
            
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
            
        return res