class Solution:
  """
  Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
  return the area of the largest rectangle in the histogram
  """
  ## ----- O(n^2) solution -> TLE (87/99 testcases passed) -----
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i, height in enumerate(heights):
            maxArea = max(maxArea, height)
            l, r = i-1, i+1
            
            while l >= 0:
                if heights[l] >= height:
                    width = i-l+1
                    maxArea = max(maxArea, height*width)
                    l -= 1
                else:
                    l += 1 
                    break
            l = max(0, l)

            while r < n:
                if heights[r] >= height:
                    width = r-l+1
                    maxArea = max(maxArea, height*width)
                    r += 1
                else:
                    r -= 1 
                    break
            
        return maxArea



    ## ----------- O(n) time solution using monotonic stack -----------
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = [-1]
        heights.append(-1)

        for i in range(n+1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                leftSmaller = stack[-1]
                rightSmaller = i

                leftDiff = idx - leftSmaller
                rightDiff = rightSmaller - idx

                width = rightDiff + leftDiff - 1
                area = heights[idx] * width
                maxArea = max(maxArea, area)
            stack.append(i)
        
        return maxArea
