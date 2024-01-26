class Solution:
  """
  You have n dice, and each dice has k faces numbered from 1 to k.

  Given three integers n, k, and target, return the number of possible ways (out of the k^n total ways) to roll the dice, 
  so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 10^9 + 7.
  """
  # ----------- Recursion + Memoization  O(n*k*target) time O(n*target) space---------------
    def solve(self, n, k, target, memo):
      # Base cases
        if target < 0:
            return 0
        if n == 0 and target == 0:
            return 1
        if n == 0 and target > 0:
            return 0
      
      # Check if value already present
        if memo[n][target] != -1:
            return memo[n][target]

        ans = 0
        for j in range(1,k+1):
            ans += self.solve(n-1, k, target-j, memo)
          
      # Store the calculated answer
        memo[n][target] = ans
        return ans

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        memo = [[-1]*(target+1) for _ in range(n+1)]
        
        return self.solve(n, k, target, memo) % MOD
      

    # ----------- Iterative O(n*k*target) time O(n*target) space -------------
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
      
        for i in range(1,n+1):
            for j in range(1,target+1):
                for x in range(1,min(j+1,k+1)):
                    dp[i][j] += dp[i-1][j-x]
                  
        return dp[-1][-1] % MOD


    # ----------- optimized Iterative O(n*k*target) time O(target) space -------------
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        prev = [0]*(target+1)
        prev[0] = 1
      
        for i in range(1,n+1):
            curr = [0]*(target+1)
            for j in range(1,target+1):
                for x in range(1,min(j+1,k+1)):
                    curr[j] += prev[j-x]
            prev = curr
                  
        return prev[-1] % MOD
      
