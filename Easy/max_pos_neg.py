class Solution:
  """
  Given an array nums sorted in non-decreasing order, 
  return the maximum between the number of positive integers and the number of negative integers.

  In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, 
  then return the maximum of pos and neg.
  
  Note that 0 is neither positive nor negative.
  """
    def maximumCount(self, nums: List[int]) -> int:
      # Find the leftmost index of an element in the array
        def leftmost(arr, target):
            lo, hi = 0, len(arr)-1
            idx = -1
            
            while lo <= hi:
                mid = (lo+hi)//2
                if arr[mid] < target:
                    lo = mid+1
                else:
                    idx = mid
                    hi = mid-1
            
            return idx

      # Find the rightmost index of an element in the array
        def rightmost(arr, target):
            lo, hi = 0, len(arr)-1
            idx = -1
            
            while lo <= hi:
                mid = (lo+hi)//2
                if arr[mid] > target:
                    hi = mid-1
                else:
                    idx = mid
                    lo = mid+1
            
            return idx

        # Locate starting and ending positions of 0
        # If no 0 is present then leftmost is index of first +ve num
        # If no 0 is present then rightmost is index of last -ve num
        start = leftmost(nums, 0)
        end = rightmost(nums, 0)

      # Check if no positive number is present
        if nums[start] < 0:
            return len(nums)
        else:
            start -= 1
            end += 1
        
        numNeg = start-0+1
        numPos = len(nums)-1-end+1
        
        return max(numNeg, numPos)
