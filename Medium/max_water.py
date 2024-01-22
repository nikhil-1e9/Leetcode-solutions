class Solution:
  """
  You are given an integer array height of length n. 
  There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

  Find two lines that together with the x-axis form a container, such that the container contains the most water.
  
  Return the maximum amount of water a container can store.
  Notice that you may not slant the container.
  """
    def maxArea(self, height: List[int]) -> int:
        ## ----------- O(n^2) solution (just passed) -------------
        n = len(height)
        max_area = 0
        
        for i in range(n):
            left = i
            right = i
            for j in range(i):
                if height[j] >= height[i]:
                    left = j
                    break
            for k in range(n-1,i,-1):
                if height[k] >= height[i]:
                    right = k
                    break
            
            max_area = max(max_area, (right-left)*height[i])

        return max_area

    def maxArea(self, height: List[int]) -> int:
        ## ------------- O(n) solution (more optimal) --------------
        n = len(height)
        max_area = 0
        i, j = 0, n-1
        while i < j:
            max_area = max(max_area, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
