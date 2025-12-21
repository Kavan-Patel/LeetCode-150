# 121. Best Time to Buy and Sell Stock

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # set the total profit
        total_profit = 0
        # set every day price
        today = prices[0]
        for i in range(1, len(prices)):
            # Count daily profit
            daily_profit = prices[i] - today
            if daily_profit < 0:
                # If daily profit is negetive then change buying day 
                # to today
                today = prices[i]
            elif daily_profit > total_profit:
                # If daily profit is more then total profit then update the 
                # total profit
                total_profit = daily_profit
        return total_profit
