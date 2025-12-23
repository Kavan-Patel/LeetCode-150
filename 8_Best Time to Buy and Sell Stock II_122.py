# 122. Best Time to Buy and Sell Stock II

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Let's find the patten in graph, if we buy and sell and is price increse in
        # next day then buy immediate after sell and again sell on next day. 
        # overall calculation should be the same for ex 1, 2, 3, 4, 5
        # buying on day 1 and selling on day 5 gives profit 4
        # also buying on day 1 selling on day 2 profit 1, again buying on day 2
        # and selling on day 3 profit 1, again buying on day 3 and selling on day 4
        # etc if we find total profit it is 4 which is same

        # Define max profit
        max_profit = 0 
        # Buying on day 1
        buy = prices[0]
        for i in range(1, len(prices)):
            # Selling on next day
            sell = prices[i]
            # Calculate local profit
            local_profit = sell - buy
            # if positive consider and add it to the max_profit
            if local_profit > 0:
                max_profit = local_profit + max_profit
            # after selling buy on the same day
            buy = prices[i]
        
        return max_profit