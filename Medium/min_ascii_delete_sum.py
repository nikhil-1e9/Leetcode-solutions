class Solution:
  """
  Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
  """
  ## ---------- Recursion + Memoization -> O(m*n) time, O(m*n) space ----------
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        def minSum(i, j):
            if i == m:
                return sum(ord(x) for x in s2[j:])
            if j == n:
                return sum(ord(x) for x in s1[i:])
            
            if (i, j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                ans = minSum(i+1, j+1)
            else:
                ans = min(ord(s2[j]) + minSum(i, j+1), ord(s1[i]) + minSum(i+1, j))
            
            memo[(i, j)] = ans
            return ans

        memo = {}
        return minSum(0, 0)


  ## ---------- Iterative solution -> O(m*n) time, O(m*n) space ----------
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] 

        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(ord(s1[i-1]) + dp[i-1][j], ord(s2[j-1]) + dp[i][j-1])
        
        return dp[-1][-1]
