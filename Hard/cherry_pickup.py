class Solution:
  """
  You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

  0 means the cell is empty, so you can pass through,
  1 means the cell contains a cherry that you can pick up and pass through, or
  -1 means the cell contains a thorn that blocks your way.

  Return the maximum number of cherries you can collect by following the rules below:

  - Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
  - After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
  - When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
  - If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.
  """
  ## -------- Most intuitive solution using Backtracking --------- ##
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Go from (0, 0) to (n-1, n-1)
        def pick(i, j, total):
            if i == n-1 and j == n-1:
                cherry = grid[i][j]
                grid[i][j] = 0
                pickAgain(i, j, total+cherry)
                grid[i][j] = cherry
                return
            if i >= n or j >= n:
                return 
            if grid[i][j] == -1:
                return 
            
            # Pick cherry
            cherry = grid[i][j]
            grid[i][j] = 0
            # Go down
            pick(i+1, j, total+cherry)
            # Go right
            pick(i, j+1, total+cherry)
            # Backtrack
            grid[i][j] = cherry

        # Go from (n-1, n-1) to (0, 0)
        def pickAgain(i, j, total):
            global maxCherry
            if i == 0 and j == 0:
                maxCherry = max(maxCherry, total)
                return
            if i < 0 or j < 0:
                return 
            if grid[i][j] == -1:
                return
            
            # Pick cherry
            cherry = grid[i][j]
            grid[i][j] = 0
            # Go up
            pickAgain(i-1, j, total+cherry)
            # Go left
            pickAgain(i, j-1, total+cherry)
            # Backtrack
            grid[i][j] = cherry

        global maxCherry
        maxCherry = 0
        pick(0, 0, 0)
        return maxCherry
      

  ## ---------- Dynamic Programming Solution ---------- ##
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Intuition -> (2 people starting from (0,0) to (n-1, n-1))
        n = len(grid)

        def doublePick(i, j, x, y):
            if i >= n or j >= n or x >= n or y >= n:
                return -1e9  # not 0 -> to reflect case where end can't be reached
            if grid[i][j] == -1 or grid[x][y] == -1:
                return -1e9  # not 0 -> to reflect case where end can't be reached
            if i == n-1 and j == n-1 and x == n-1 and y == n-1:
                return grid[i][j]  # return any of them because both reach end at same time due to symmetric grid
            
            # If this state is already cached return it
            if (i, j, x, y) in memo:
                return memo[(i, j, x, y)]

            # 1st down, 2nd down
            dd = doublePick(i+1, j, x+1, y)
            # 1st down, 2nd right
            dr = doublePick(i+1, j, x, y+1)
            # 1st right, 2nd down
            rd = doublePick(i, j+1, x+1, y)
            # 1st right, 2nd right
            rr = doublePick(i, j+1, x, y+1)

            # If both arrive at same index only add one of them
            if i == x and j == y:
                cherries = grid[i][j]
            else:
                cherries = grid[i][j] + grid[x][y]
            
            # Cache the result
            memo[(i, j, x, y)] = cherries + max(dd, dr, rd, rr)
            return memo[(i, j, x, y)]

        memo = {}
        ans = doublePick(0, 0, 0, 0)
        # if no path exists return 0
        return ans if ans > 0 else 0
