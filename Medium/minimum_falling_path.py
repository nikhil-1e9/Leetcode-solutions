class Solution:
  """
  Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
  A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. 
  Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
  """
    ## ------------------- Solution using recursion and memoization O(n^2) time and O(n^2) space complexity-------------------
    def minPath(self, matrix, i, j, n, ans):
        # Out of bound case
        if j < 0 or j > n-1:
            return 1e9
        # Base case
        if i == 0:
            return matrix[0][j]
        # Memoize the solution
        if (i,j) not in ans:
            ans[(i,j)] = matrix[i][j] + min(self.minPath(matrix, i-1, j-1, n, ans),
                                  self.minPath(matrix, i-1, j, n, ans),
                                  self.minPath(matrix, i-1, j+1, n, ans))
        return ans[(i,j)]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ## ---------------- Recursive solution -----------------
        n = len(matrix)
        ans = {}
        minSum = 1e9
        # Find the minimum element in the last row
        for j in range(n):
            minSum = min(minSum, self.minPath(matrix, n-1, j, n, ans))
        return minSum


    ## ---------------- Iterative solution using dp array --------------------
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    ## ------------------- Starting from bottom -------------------
        n = len(matrix)
        dp = [[1e9]*(n+2) for _ in range(n+1)]
        dp[-1] = [0]*(n+2)
        for i in range(n-1,-1,-1):
            for j in range(1,n+1):
                dp[i][j] = matrix[i][j-1] + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])
        # print(dp)
        return min(dp[0])


    ## ------------------ Iterative solution using dp array -----------------------
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    ## ------------------- Starting from top --------------------
        n = len(matrix)
        dp = [[1e9]*(n+2) for _ in range(n)]
        dp[0] = [1e9]+matrix[0]+[1e9]
        for i in range(1,n):
            for j in range(1,n+1):
                dp[i][j] = matrix[i][j-1] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        # print(dp)
        return min(dp[-1])


  ## ------------------ Iterative solution using O(n) space -----------------------
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
      ## ---------- Starting from bottom -----------
        n = len(matrix)
        curr = [1e9]*(n+2)
        prev = [0]*(n+2)
        for i in range(n-1,-1,-1):
            for j in range(1,n+1):
                curr[j] = matrix[i][j-1] + min(prev[j-1], prev[j], prev[j+1])
            # print(curr)
            # print(prev)
            prev[:] = curr
        return min(prev)


    ## ------------------ Iterative solution using O(1) extra space -----------------------
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    ## Starting from top with no extra space
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0,j-1)], 
                                    matrix[i-1][j],
                                    matrix[i-1][min(n-1,j+1)])
        return min(matrix[-1])
