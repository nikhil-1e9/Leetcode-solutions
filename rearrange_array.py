class Solution:
  """
  You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

  You should rearrange the elements of nums such that the modified array follows the given conditions:

  - Every consecutive pair of integers have opposite signs.
  - For all integers with the same sign, the order in which they were present in nums is preserved.
  - The rearranged array begins with a positive integer.
  - Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
  """
  ## ---------------- Recursive ---------------- ##
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def rearrange(pos, neg):
            if pos >= n or neg >= n:
                return ans
            
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            
            ans.append(nums[pos])
            ans.append(nums[neg])
            rearrange(pos+1, neg+1)
        
        ans = []
        rearrange(0, 0)
        return ans

   ## ------------- Iterative ------------ ##
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = 0, 0
        ans = []

        while pos < n and neg < n:
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            
            ans.append(nums[pos])
            ans.append(nums[neg])
            pos += 1
            neg += 1
        
        return ans
