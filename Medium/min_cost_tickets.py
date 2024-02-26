class Solution:
  """
  You have planned some train traveling one year in advance. 
  The days of the year in which you will travel are given as an integer array days. 
  Each day is an integer from 1 to 365.

  Train tickets are sold in three different ways:
  
  - a 1-day pass is sold for costs[0] dollars,
  - a 7-day pass is sold for costs[1] dollars, and
  - a 30-day pass is sold for costs[2] dollars.
  The passes allow that many days of consecutive travel.
  
  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
  Return the minimum number of dollars you need to travel every day in the given list of days.
  """
  ## ------------ Top down DP (recursion + memoization) --------------
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        def minCost(i):
            if i == n:
                return 0
            
            if i in memo:
                return memo[i]

            day = days[i]
            oneIdx = sevenIdx = thirtyIdx = i+1
            
            while sevenIdx < n and day + 7 > days[sevenIdx]:
                sevenIdx += 1
            
            while thirtyIdx < n and day + 30 > days[thirtyIdx]:
                thirtyIdx += 1
            
            memo[i] = min(costs[0] + minCost(oneIdx),
                          costs[1] + minCost(sevenIdx),
                          costs[2] + minCost(thirtyIdx))
            
            return memo[i]
        
        memo = {}
        return minCost(0)


  ## ------------ Bottom up DP (tabulation) --------------
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        days = set(days)
        
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            
            dp[i] = min(dp[max(0,i-1)] + costs[0], 
                        dp[max(0,i-7)] + costs[1], 
                        dp[max(0,i-30)] + costs[2])
        
        return dp[-1]
