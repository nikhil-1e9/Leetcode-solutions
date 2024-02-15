class Solution:
  """
  Given an integer array nums, return the number of triplets chosen from the array 
  that can make triangles if we take them as side lengths of a triangle.
  """
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        valid = 0

        for k in range(n-1, 1, -1):
            l, r = 0, k-1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    valid += r-l
                    r -= 1
                else:
                    l += 1

        return valid
