class Solution:
  """
  Given a triangle array, return the minimum path sum from top to bottom.

  For each step, you may move to an adjacent number of the row below. 
  More formally, if you are on index i on the current row, 
  you may move to either index i or index i + 1 on the next row.
  """
  ## -------- Top Down DP -> O(n^2) time, O(n^2) space -------- ##
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        def minPathSum(i, j):
            if i == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = triangle[i][j] + min(minPathSum(i+1, j), minPathSum(i+1, j+1))
            return memo[(i, j)]

        memo = {}
        return minPathSum(0, 0)


  ## ------- Bottom Up DP -> O(n^2) time, O(n^2) space ------- ##
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for _ in range(i)] for i in range(1, n+2)]
        
        for i in range(n-1,-1,-1):
            for j in range(i+1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]


  ## ----- Bottom Up DP (space optimized) -> O(n^2) time, O(n) space ----- ##
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        nxt = [0]*(n+1)
        
        for i in range(n-1,-1,-1):
            cur = [0]*(i+1)
            for j in range(i+1):
                cur[j] = triangle[i][j] + min(nxt[j], nxt[j+1])
            nxt = cur
        
        return nxt[0]


  ## ----- Bottom Up DP (no extra space) -> O(n^2) time, O(1) space ----- ##
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i-1][min(i-1, j)], triangle[i-1][max(0, j-1)])
        
        return min(triangle[-1])
  
