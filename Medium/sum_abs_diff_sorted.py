class Solution:
  """
  You are given an integer array nums sorted in non-decreasing order.

  Build and return an integer array result with the same length as nums 
  such that result[i] is equal to the summation of absolute differences 
  between nums[i] and all the other elements in the array.
  
  In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 
  0 <= j < nums.length and j != i (0-indexed).
  """
  ## ------- Brute Force solution -> O(n^2) time, O(1) extra space ------- ##
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        
        for i in range(n):
            for j in range(n):
                res[i] += abs(nums[i]-nums[j]) 
        
        return res


  ## -------- Optimized solution -> O(n) time, O(n) extra space -------- ##
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preSum = [0]*(n+1)
        res = [0]*n

        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        
        for i in range(n):
            leftSum = preSum[i]
            rightSum = preSum[n] - preSum[i+1]
            eleSum = (2*i+1 - n) * nums[i]
            res[i] = rightSum - leftSum + eleSum
        
        return res
