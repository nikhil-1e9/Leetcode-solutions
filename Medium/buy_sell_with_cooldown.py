class Solution:
  """
  You are given an array prices where prices[i] is the price of a given stock on the ith day.

  Find the maximum profit you can achieve. You may complete as many transactions as you like 
  (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
  
  - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
  
  Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
  """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def buySell(i, buy):
            # no more days to trade
            if i >= n:
                return 0
            
            # If state already in cache no need to compute again
            if (i, buy) in memo:
                return memo[(i, buy)]

            # If the stock is brought on some previous day
            # we can either sell on current day or skip this day
            if buy:
                # sell condition with cooldown of 1 day
                sell = buySell(i+2, not buy) + prices[i]
                # skipped current day and move to next
                skip = buySell(i+1, buy)
                # maximum of the two
                ans = max(sell, skip)
            
            # If the stock has not been brought on some previous day
            # we can either buy it on currrent day or skip this day
            else:
                # buy condition 
                Buy = buySell(i+1, not buy) - prices[i]
                # # skipped current day and move to next
                skip = buySell(i+1, buy)
                # maximum of the two
                ans = max(Buy, skip)
            
            # Store the state in a global cache
            memo[(i, buy)] = ans
            return ans
        
        memo = {}
        return buySell(0, False) # buy cond False initially because nothing is bought
