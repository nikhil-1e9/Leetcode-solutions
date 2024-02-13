class Solution:
  """
  Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

  You have the following three operations permitted on a word:

  - Insert a character
  - Delete a character
  - Replace a character
  """
  ## ---------- Recursion + Memoization ----------- ##
  ## ---------- O(m*n) time , O(m*n) space -------- ##
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        def edit(i, j):
            # Base cases
            if i >= m:
                return n-j
            if j >= n:
                return m-i
            
            if (i, j) in memo:
                return memo[(i, j)]

            # If the characters are equal no operations are needed
            if word1[i] == word2[j]:
                nothing = edit(i+1, j+1)
                ans = nothing
            else:
                delete = edit(i+1, j)       # Delete character
                replace = edit(i+1, j+1)    # Replace character
                insert = edit(i, j+1)       # Insert character
                ans = 1 + min(delete, replace, insert)
            
            memo[(i, j)] = ans
            return ans
            
        memo = {}
        return edit(0, 0)


    ## ---------- Tabulation DP ----------- ##
    ## ---------- O(m*n) time , O(m*n) space -------- ##
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        dp[0] = [j for j in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    insert = dp[i][j-1]
                    
                    dp[i][j] = 1 + min(delete, replace, insert)
        
        return dp[-1][-1]


  ## ---------- Tabulation + Space optimization ----------- ##
    ## ---------- O(m*n) time , O(n) space -------- ##
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [j for j in range(n+1)]

        for i in range(1, m+1):
            curr = [0]*(n+1)
            curr[0] = i
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    delete = prev[j]    
                    replace = prev[j-1] 
                    insert = curr[j-1]  
                  
                    curr[j] = 1 + min(delete, replace, insert)
            
            prev = curr
        
        return prev[-1] 
