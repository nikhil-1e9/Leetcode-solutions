class Solution:
  """
  You are climbing a staircase. It takes n steps to reach the top.
  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
  """
  #------------------- 4 approaches to solve this problem ---------------#
    
  ## ---------------- 1st approach --------------- 
    ## Using simple recursion -> O(2^n) time complexity
    # This approach gives TLE for larger values of n
    def climbStairs(self, n: int) -> int:
        return self.climbStairs(n-1) + self.climbStairs(n-2)
      
  ## ---------------- 2nd approach --------------- 
    ## Memoized top down DP -> O(n) time O(n)+O(n) space for recursion stack and for ans array
    def solve(self, n, ans):
        if n == 1 or n == 0:
            return 1
        if ans[n] == -1:
            ans[n] = self.solve(n-1, ans) + self.solve(n-2, ans)
        return ans[n]

    def climbStairs(self, n: int) -> int:
        ans = [-1]*(n+1)
        return self.solve(n, ans)

  ## ---------------- 3rd approach ---------------     
    ## Bottom up DP (iterative solution) -> O(n) time and O(n) space complexity for the array
    def climbStairs(self, n: int) -> int:
        ans = [1]*(n+1)
        for i in range(2,n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]

  ## ---------------- 4th approach --------------- (Most optimized)
    ## Using 2 variables instead of the full array -> O(n) time and O(1) space complexity
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2
        for _ in range(n-1):
            prev, curr = curr, prev+curr
        return prev
