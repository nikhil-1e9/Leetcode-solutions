class Solution:
  """
  A message containing letters from A-Z can be encoded into numbers using the following mapping:

  'A' -> "1"
  'B' -> "2"
  ...
  'Z' -> "26"
  To decode an encoded message, all the digits must be grouped then mapped back into letters 
  using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
  
  - "AAJF" with the grouping (1 1 10 6)
  - "KJF" with the grouping (11 10 6)
  
  Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
  
  Given a string s containing only digits, return the number of ways to decode it.
  
  The test cases are generated so that the answer fits in a 32-bit integer.
  """
  ## -------- Recursion + Memoization --------- ##
    def numDecodings(self, s: str) -> int:
        def decode(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]

            ans = decode(i+1)
            if i+2 <= len(s) and 0 < int(s[i:i+2]) <= 26:
                ans += decode(i+2)
            
            memo[i] = ans
            return ans
        
        memo = {}
        return decode(0)


  ## --------- Bottom up DP --------- ##
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1

        for i in range(n-1,-1,-1):
            dp[i] = dp[i+1]
            if i+2 <= len(s) and 0 < int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
            if s[i] == '0':
                dp[i] = 0

        return cur


  ## --------- Bottom up DP (space optimized) --------- ##
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cur, nxt, last = 0, 1, 0

        for i in range(n-1,-1,-1):
            cur = nxt
            if i+2 <= len(s) and 0 < int(s[i:i+2]) <= 26:
                cur += last 
            if s[i] == '0':
                cur = 0 

            nxt, last = cur, nxt 

        return cur
