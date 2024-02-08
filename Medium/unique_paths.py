class Solution:
  """
  There is a robot on an m x n grid. 
  The robot is initially located at the top-left corner (i.e., grid[0][0]). 
  The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
  The robot can only move either down or right at any point in time.

  Given the two integers m and n, 
  return the number of possible unique paths that the robot can take to reach the bottom-right corner.

  The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
  """
  # ------------ Recursion only approach O(2^max(m,n)) ------------
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0
        
        if m == 1 and n == 1:
            return 1
        
        self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

  
  # --------- Recursion + Memoization -> O(m*n) time O(m*n) space ----------
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def solve(x, y):
            if x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            
            if (x, y) in memo:
                return memo[(x, y)]

            memo[(x, y)] = solve(x+1, y) + solve(x, y+1)
            return memo[(x, y)]
        
        return solve(0, 0)


  ## ----- Bottom up DP Tabulation -> O(m*n) time O(n) space ----- ##
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1]*n

        for i in range(1, m):
            curr = [0]*n
            curr[0] = 1
            
            for j in range(1, n):
                curr[j] = prev[j] + curr[j-1]
            
            prev = curr
        
        return prev[-1]
    
