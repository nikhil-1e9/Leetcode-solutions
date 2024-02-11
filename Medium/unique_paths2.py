class Solution:
  """
  You are given an m x n integer array grid. 
  There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
  The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
  The robot can only move either down or right at any point in time.

  An obstacle and space are marked as 1 or 0 respectively in grid. 
  A path that the robot takes cannot include any square that is an obstacle.

  Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

  The testcases are generated so that the answer will be less than or equal to 2 * 10^9.
  """
  ## --- Top Down DP -> Recursion + Memoization -> O(m*n) time, O(m*n) space --- ##
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def numPaths(x, y):
            if x >= m or y >= n:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            if x == m-1 and y == n-1:
                return 1
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            memo[(x, y)] = numPaths(x+1, y) + numPaths(x, y+1)
            return memo[(x, y)]
        
        memo = {}
        return numPaths(0, 0)

 ## ------- Bottom up DP -> Tabulation -> O(m*n) time, O(m*n) space ------- ##
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # Base cases
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else: break
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else: break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[-1][-1]

  
  ## --- Bottom up DP(space optimized) -> O(m*n) time, O(n) space ---
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0]*n
        # Base case
        for j in range(n):
            if obstacleGrid[0][j] != 1:
                prev[j] = 1
            else: break
        
        for i in range(1, m):
            curr = [0]*n
            if prev[0] == 1:
                curr[0] = 1-obstacleGrid[i][0]
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    curr[j] = prev[j] + curr[j-1]
                else:
                    curr[j] = 0
                
            prev = curr
        
        return prev[-1]        
