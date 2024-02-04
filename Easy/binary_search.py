class Solution:
  """
  Given an array of integers nums which is sorted in ascending order, and an integer target, 
  write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

  You must write an algorithm with O(log n) runtime complexity.
  """
  # -------------- Iterative Binary search ---------------
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            
        return -1


  # -------------- Recursive Binary search ---------------
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, target, left, right):
            if left > right:
                return -1

            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            
            if arr[mid] > target:
                return binarySearch(arr, target, left, mid-1)
            else:
                return binarySearch(arr, target, mid+1, right)

        return binarySearch(nums, target, 0, len(nums)-1)

  
  # -------------- Using bisect method ---------------
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx
        
        return -1
