class Solution:
  """
  Given an array of integers temperatures represents the daily temperatures, 
  return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
  If there is no future day for which this is possible, keep answer[i] == 0 instead.
  """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## -------- Brute Force O(n^2) time complexity ---------
        n = len(temperatures)
        ans = []
        
        for i,temp in enumerate(temperatures):
            for j in range(i+1, n):
                if temperatures[j] > temp:
                    ans.append(j-i)
                    break
            
            if len(ans) != i+1:
                ans.append(0)
        
        return ans


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## -------------- O(n) using monotonic stack -----------------
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                idx = stack[-1]
                ans[idx] = i-stack.pop()
            
            stack.append(i)
        
        return ans
