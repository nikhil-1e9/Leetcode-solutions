class Solution:
  """
  Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

  A subsequence of a string is a new string generated from the original string with some characters (can be none) 
  deleted without changing the relative order of the remaining characters.

  For example, "ace" is a subsequence of "abcde".
  A common subsequence of two strings is a subsequence that is common to both strings.
  """
    # -------------- Recursion + Memoization -> O(n^2) space O(n^2) time ----------------
    def LCS(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]

        if s1[i] == s2[j]:
            ans = 1 + self.LCS(s1, s2, i+1, j+1)
        else:
            ans = max(self.LCS(s1,s2,i,j+1), self.LCS(s1,s2,i+1,j))
        
        memo[i][j] = ans
        return memo[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        global memo
        memo = [[-1]*n for _ in range(m)]
        return self.LCS(text1, text2, 0, 0)


    # ---------------- Iterative -> O(n^2) space O(n^2) time ----------------
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]

      
    # ---------------- Iterative -> O(n) space O(n^2) time ----------------
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0]*(n+1)
        curr = [0]*(n+1)
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1+prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr[:]
        
        return prev[-1]
