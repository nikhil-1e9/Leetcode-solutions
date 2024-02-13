class Solution:
  """
  Given an array nums with n objects colored red, white, or blue, 
  sort them in-place so that objects of the same color are adjacent, 
  with the colors in the order red, white, and blue.

  We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

  You must solve this problem without using the library's sort function.
 
  """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums)-1
        
        while j <= k:
            if nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
