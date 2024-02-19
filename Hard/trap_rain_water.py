class Solution:
  """
  Given n non-negative integers representing an elevation map 
  where the width of each bar is 1, compute how much water it can trap after raining.
  """
  ## ----------- O(n^2) time solution ----------- ## 
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        
        for i, h in enumerate(height):
            maxLeft, maxRight = -1, -1
            l, r = i, i
            
            while l >= 0:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                l -= 1
            if maxLeft == h:
                continue
            
            while r < n:
                if height[r] > maxRight:
                    maxRight = height[r]
                r += 1
            if maxRight == h:
                continue
            
            water += min(maxLeft, maxRight) - h

        return water


  ## ----------- O(n) time solution ----------- ## 
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0
        maxLeft, maxRight = [0]*n, [0]*n
        curmaxL, curmaxR = 0, 0
        
        for i in range(n):
            curmaxL = max(curmaxL, height[i])
            maxLeft[i] = curmaxL
        
        for i in range(n-1,-1,-1):
            curmaxR = max(curmaxR, height[i])
            maxRight[i] = curmaxR
        
        for i in range(n):
            water += min(maxLeft[i], maxRight[i]) - height[i]

        return water
