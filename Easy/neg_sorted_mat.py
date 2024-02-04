class Solution:
  """
  Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
  return the number of negative numbers in grid.
  """
  # Use Binary Search in each row O(m * log n) time complexity
    def countNegatives(self, grid: List[List[int]]) -> int:
        def findFirstNegative(arr):
            lo, hi = 0, len(arr)-1
            idx = len(arr)
            
            while lo <= hi:
                mid = (lo+hi)//2
                if arr[mid] >= 0:
                    lo = mid+1
                else:
                    idx = mid
                    hi = mid-1
            
            return idx
        
        m, n = len(grid), len(grid[0])
        neg = 0
        
        for row in grid:
            neg += n - findFirstNegative(row)
        
        return neg

  # O(m+n) solution -> works because both rows and columns are sorted
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        neg = 0
        row, col = m-1, 0
        
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                neg += n - col
                row -= 1
            else:
                col += 1
        
        return neg
