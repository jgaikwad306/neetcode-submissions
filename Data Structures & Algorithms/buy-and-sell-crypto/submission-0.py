class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = prices[0]
        max_position = 0
        min = prices[0]
        min_position = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > profit:
                max = prices[i]
                profit = max - min
        return profit
        