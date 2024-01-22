class Solution:
  """
  You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
  the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
  and it will automatically contact the police if two adjacent houses were broken into on the same night.
  
  Given an integer array nums representing the amount of money of each house, 
  return the maximum amount of money you can rob tonight without alerting the police.
  """
  ## ------ Recursive solution (Top down DP + memoization) ------
    ## Starting from end of array
    def maxMoney(self, nums, n, i, ans):
        if i < 0:
            return 0
          
        if i not in ans:
            ans[i] = max(nums[i]+self.maxMoney(nums,n,i-2,ans), self.maxMoney(nums,n,i-1,ans))
        return ans[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = {}
        return self.maxMoney(nums, n, n-1, ans)

  ## ------ Iterative solution (Bottom up DP) O(n) space ------
    def rob(self, nums: List[int]) -> int:
        if n==1: 
            return nums[0]
          
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
      
        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]


  ## ------ Iterative solution (Bottom up DP) O(1) space ------
    def rob(self, nums: List[int]) -> int:
        if n==1: 
            return nums[0]
          
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])
      
        for i in range(2,n):
            curr = max(nums[i]+prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
