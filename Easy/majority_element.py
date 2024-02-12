class Solution:
  """
  Given an array nums of size n, return the majority element.

  The majority element is the element that appears more than ⌊n / 2⌋ times. 
  You may assume that the majority element always exists in the array.
  """
  ## ---------- O(nlogn) time, O(1) space ------------- ##
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


  ## ---------- O(n) time, O(n) space ------------- ##
    def majorityElement(self, nums: List[int]) -> int:
        ans = {}
        for x in nums:
            ans[x] = ans.get(x, 0) + 1
        for i in ans:
            if ans[i] > len(nums)//2:
                return i

  ###---------- Moore's voting algorithm -----------###
  ## ---------- O(n) time, O(1) space ------------- ##
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if count == 0:
                ans = x
            if x == ans:
                count += 1
            else:
                count -= 1
        return ans
