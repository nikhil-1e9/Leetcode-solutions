class Solution:
  """
  You are given an m x n integer matrix matrix with the following two properties:

  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the previous row.
  - Given an integer target, return true if target is in matrix or false otherwise.
  
  You must write a solution in O(log(m * n)) time complexity.
  """
  ## ------------ O(log(m*n)) time, O(m*n) space -------------- ##
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr += row

        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False

## --------------------------------------------------------------------------- ##

  ## ------------------- O(log(m*n)) time, O(1) space --------------------- ##
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        
        while l <= r:
            mid = (l + r) // 2
            x, y = mid // n, mid % n
            
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False
