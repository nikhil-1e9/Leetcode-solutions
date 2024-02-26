class Solution:
  """
  Given an array of integers nums, return the number of good pairs.

  A pair (i, j) is called good if nums[i] == nums[j] and i < j.
  """
  ## ------ Brute Force -> O(n^2) time, O(1) space ------ ##
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        pairs = 0

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    pairs += 1
        
        return pairs
      

  ## ------ ## Optimal approach -> O(n) time, O(n) space ----- ##
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = defaultdict(int)
        pairs = 0

        for num in nums:
            pairs += dic[num]
            dic[num] += 1
        
        return pairs
