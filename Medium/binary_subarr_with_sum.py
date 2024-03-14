class Solution:
  """
  Given a binary array nums and an integer goal, 
  return the number of non-empty subarrays with a sum goal.

  A subarray is a contiguous part of the array.
  """  
  ## ---------- Brute Force -> O(n^2) time, O(1) space ---------- ##
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            subSum = 0
            for j in range(i, n):
                subSum += nums[j]
                ans += subSum == goal
        
        return ans

        
  ## --------- Prefix sum + Hashing -> O(n) time, O(n) space --------- ##
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = {0: 1}
        curSum = 0
        ans = 0

        for num in nums:
            curSum += num
            if curSum - goal in prefix:
                ans += prefix[curSum - goal]
            prefix[curSum] = prefix.get(curSum, 0) + 1
        
        return ans

  ## ----------- Sliding Window -> O(n) time, O(1) space ----------- ##
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int: 
        n = len(nums)
        
        def subarrSumAtMostK(k):
            if k < 0:
                return 0

            subCount = 0
            curSum = 0
            l, r = 0, 0
            
            while r < n:
                curSum += nums[r]
                while curSum > k:
                    curSum -= nums[l]
                    l += 1
                subCount += r-l+1
                r += 1
            
            return subCount
        
        return subarrSumAtMostK(goal) - subarrSumAtMostK(goal-1)
