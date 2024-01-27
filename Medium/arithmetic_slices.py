class Solution:
  """
  An integer array is called arithmetic if it consists of at least three elements 
  and if the difference between any two consecutive elements is the same.

  For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
  Given an integer array nums, return the number of arithmetic subarrays of nums.
  
  A subarray is a contiguous subsequence of the array.
  """
  # ---------- Brute Force Solution O(n^3) time complexity--------------
  # Check every subarray of length >= 3 to be arithmetic
    def isArithmetic(self, arr):
        diff = arr[0]-arr[1]
        for i in range(1,len(arr)-1):
            if arr[i] - arr[i+1] != diff:
                return False
        return True

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return 0
        
        count = 0
        
        for i in range(n):
            for j in range(i+3,n+1):
                if self.isArithmetic(nums[i:j]):
                    count += 1
        return count

  # ------------ Optimized solution O(n) time complexity --------------
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # if n <= 2:
        #     return 0
        
        count = 0
        subCount = 0
        for i in range(1,n-1):
            if nums[i]-nums[i-1] == nums[i+1]-nums[i]:
                subCount += 1
                count += x
            else:
                subCount = 0

        return count
