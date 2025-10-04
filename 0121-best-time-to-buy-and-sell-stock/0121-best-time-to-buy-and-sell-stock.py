class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                
            else:
                left = right

            right += 1
            maxProfit = max(maxProfit, profit)


        return maxProfit
        