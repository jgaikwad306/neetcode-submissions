class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = prices[0]
        min = prices[0]
        profit = 0
        for price in prices:
            if price < min:
                min = price
            if price - min > profit :
                max = price
                profit = max - min
        return profit
            
        
        