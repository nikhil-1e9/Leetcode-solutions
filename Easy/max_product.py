class Solution:
  """
  Given the array of integers nums, you will choose two different indices i and j of that array. 
  Return the maximum value of (nums[i]-1)*(nums[j]-1).
  """
  ## --------- O(n^2) time, O(1) space --------- ##
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                maxVal = max(maxVal, (nums[i]-1)*(nums[j]-1))
        
        return maxVal


  ## --------- O(nlogn) time, O(1) space -------- ##
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]-1) * (nums[1]-1)



  ## --------- O(n) time, O(1) space --------- ##
    def maxProduct(self, nums: List[int]) -> int:
        firstMax, secondMax = 0, 0
        for num in nums:
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
            elif num > secondMax:
                secondMax = num
        
        return (firstMax-1) * (secondMax-1)
