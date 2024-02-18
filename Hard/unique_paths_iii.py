class Solution:
  """
  You are given an m x n integer array grid where grid[i][j] could be:

  - 1 representing the starting square. There is exactly one starting square.
  - 2 representing the ending square. There is exactly one ending square.
  - 0 representing empty squares we can walk over.
  - -1 representing obstacles that we cannot walk over.
  
  Return the number of 4-directional walks from the starting square to the ending square, 
  that walk over every non-obstacle square exactly once.
  """
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        zeros = 0

        # Count non-obstacle paths and find where to start
        for i in range(m):
            for j in range(n):
                zeros += grid[i][j] == 0
                if grid[i][j] == 1:
                    xStart, yStart = i, j

        def walk(x, y, steps, visited):
            global ans
            # Out of bounds case
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            # Hitting obstacle
            if grid[x][y] == -1:
                return
            # Don't go if location already visited
            if (x, y) in visited:
                return
            # Reached ending location 
            if grid[x][y] == 2:
                # Check if all non-obstacles travelled exactly once
                if steps == zeros + 1:   # +1 due to counting of ending point
                    ans += 1
                visited = set()
                return 

            # Mark current square as visited
            visited.add((x, y))
            # Try going up
            walk(x-1, y, steps+1, visited)
            # Try going left
            walk(x, y-1, steps+1, visited)
            # Try going right
            walk(x, y+1, steps+1, visited)
            # Try going down
            walk(x+1, y, steps+1, visited)
            # Backtrack
            visited.discard((x, y))

        global ans
        ans = 0
        
        walk(xStart, yStart, 0, set())
        return ans
