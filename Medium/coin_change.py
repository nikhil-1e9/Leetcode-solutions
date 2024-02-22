class Solution:
  """
  You are given an integer array coins representing coins of different denominations 
  and an integer amount representing a total amount of money.

  Return the fewest number of coins that you need to make up that amount. 
  If that amount of money cannot be made up by any combination of the coins, return -1.
  
  You may assume that you have an infinite number of each kind of coin.
  """
  ## --------- Top Down DP (Recursion + Memoization) approach --------- ##
    # ---------- O(n*amount) time, O(n*amount) space ----------- #
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def minCoins(i, total):
            if i == n or total < 0:
                return 1e9
            if total == 0:
                return 0

            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = min(1 + minCoins(i, total-coins[i]), minCoins(i+1, total))
            return memo[(i, total)]

        memo = {}
        ans = minCoins(0, amount)
        return ans if ans <= 10**4 else -1

        
  ## --------- Bottom up DP (Tabulation) approach --------- ##
  # ---------- O(n*amount) time, O(n*amount) space ----------- #
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for j in range(1, amount+1):
            dp[0][j] = 1e9

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0:
                    take = 1 + dp[i][j-coins[i-1]]
                else:
                    take = 1e9
                
                notTake = dp[i-1][j]
                dp[i][j] = min(take, notTake)
        
        ans = dp[-1][-1]
        return ans if ans <= 10**4 else -1

  ## --------- Memory Optimized iterative solution --------- ##
  # ---------- O(n*amount) time, O(amount) space ----------- #
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        prev = [1e9]*(amount+1)
        prev[0] = 0

        for i in range(1, n+1):
            curr = [0]*(amount+1)
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0:
                    take = 1 + curr[j-coins[i-1]]
                else:
                    take = 1e9
                
                notTake = prev[j]
                curr[j] = min(take, notTake)
            
            prev = curr
        
        ans = prev[-1]
        return ans if ans <= 10**4 else -1
