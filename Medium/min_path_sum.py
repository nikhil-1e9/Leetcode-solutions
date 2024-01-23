class Solution:
  """
  Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

  Note: You can only move either down or right at any point in time.
  """
    # -------------- Initialising dp array with 0s and large numbers ----------------
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
      
        dp = [[0]*(n+1) for _ in range(m+1)]  
        dp[1][1] = grid[0][0]
        dp[0] = [1e9]*(n+1)
        for i in range(m+1):
            dp[i][0] = 1e9
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    continue
                
                dp[i][j] = grid[i-1][j-1] + min(dp[i][j-1], dp[i-1][j])
              
        return dp[-1][-1]

    # -------- Using grid elements in dp array -----------
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
      # Populating dp array by adding grid elements
        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i-1][j-1]
                else:
                    dp[i][j] = 1e9

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    continue
                
                dp[i][j] += min(dp[i][j-1], dp[i-1][j])
              
        return dp[-1][-1]

        
    # ------------ O(1) extra space solution --------------
    def minPathSum(self, grid: List[List[int]]) -> int:
        ## Changing the grid array in place
        # This works because the first row and first column in previous solutions
        # consider the minimum of left and up elements and in those one of the elements 
        # is a big number so just adding the previous row or column element is enough
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
