class Solution:
  """
  The chess knight has a unique movement, it may move two squares vertically 
  and one square horizontally, or two squares horizontally and 
  one square vertically (with both forming the shape of an L). 
  The possible movements of chess knight are shown in this diagram:

  A chess knight can move as indicated in the chess diagram below:

  We have a chess knight and a phone pad as shown below, 
  the knight can only stand on a numeric cell (i.e. blue cell).

  Given an integer n, return how many distinct phone numbers of length n we can dial.

  You are allowed to place the knight on any numeric cell initially and 
  then you should perform n - 1 jumps to dial a number of length n. 
  All jumps should be valid knight jumps.

  As the answer may be very large, return the answer modulo 10^9 + 7.
  """
  ## Top Down (Recursion + Memoization) -> O(12*n) time, O(12*n) space ##
    def knightDialer(self, n: int) -> int:
        MOD = 10**9+7

        def moveKnight(x, y, n):
            if x < 0 or x > 3:
                return 0
            if y < 0 or y > 2:
                return 0
            if x == 3 and (y == 0 or y == 2):
                return 0
            if n == 1:
                return 1
            
            if (x, y, n) in memo:
                return memo[(x, y, n)]

            moves = moveKnight(x+1, y-2, n-1) + moveKnight(x+1, y+2, n-1) +\
                    moveKnight(x-1, y-2, n-1) + moveKnight(x-1, y+2, n-1) +\
                    moveKnight(x+2, y-1, n-1) + moveKnight(x+2, y+1, n-1) +\
                    moveKnight(x-2, y-1, n-1) + moveKnight(x-2, y+1, n-1)
            
            memo[(x, y, n)] = moves
            return moves
          
        ans = 0
        memo = {}
        for x in range(3):
            for y in range(3):
                ans = (ans + moveKnight(x, y, n)) % MOD
        ans = (ans + moveKnight(3, 1, n)) % MOD

        return ans

# --------------------------------------------------------------------------- #

  ## Bottom up (Tabulation) -> O(12*n) time, O(12) space ##
    def knightDialer(self, n: int) -> int:
        dp = [[1,1,1],[1,1,1],[1,1,1],[0,1,0]]
        
        def valid(x, y):
            if x < 0 or x > 3:
                return False
            if y < 0 or y > 2:
                return False
            if x == 3 and (y == 0 or y == 2):
                return False
            return True

        for i in range(1, n):
            curr = [[1,1,1],[1,1,1],[1,1,1],[0,1,0]]
            for x in range(4):
                for y in range(3):
                    if x == 3 and (y == 2 or y == 0):
                        continue
                    val = 0
                    if valid(x-2, y-1):
                        val += dp[x-2][y-1]
                    if valid(x-2, y+1):
                        val += dp[x-2][y+1]
                    if valid(x-1, y-2):
                        val += dp[x-1][y-2]
                    if valid(x-1, y+2):
                        val += dp[x-1][y+2]
                    if valid(x+1, y-2):
                        val += dp[x+1][y-2]
                    if valid(x+1, y+2):
                        val += dp[x+1][y+2]
                    if valid(x+2, y-1):
                        val += dp[x+2][y-1]
                    if valid(x+2, y+1):
                        val += dp[x+2][y+1]
                    curr[x][y] = val % MOD
            dp = curr
        
        ans = 0
        for x in range(3):
            for y in range(3):
                ans = (ans + dp[x][y]) % MOD
        ans = (ans + dp[3][1]) % MOD
    
        return ans
