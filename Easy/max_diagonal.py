class Solution:
  """
  You are given a 2D 0-indexed integer array dimensions.

  For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents the width of the rectangle i.
  Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest diagonal, 
  return the area of the rectangle having the maximum area.
  """
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        for l,b in dimensions:
            diag = l*l + b*b
            if diag > max_diag:
                max_diag = diag
                max_area = l*b
            elif diag == max_diag:
                max_area = max(max_area, l*b)
        return max_area
