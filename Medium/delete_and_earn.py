class Solution:
  """
  You are given an integer array nums. You want to maximize the number of 
  points you get by performing the following operation any number of times:

  - Pick any nums[i] and delete it to earn nums[i] points. 
    Afterwards, you must delete every element equal to 
    nums[i] - 1 and every element equal to nums[i] + 1.
  
  Return the maximum number of points you can earn by applying the above operation some number of times.
  """
  ## Top Down (Recursion + Memoization) -> O(n*logn) time, O(n^2) space ##
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        def maxPoints(i, prev):
            if i == n:
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]

            notTake = maxPoints(i+1, prev)
            take = 0
            if prev == -1 or (nums[i] != prev-1 and nums[i] != prev+1):
                take = nums[i] + maxPoints(i+1, nums[i])
            
            memo[(i, prev)] = max(take, notTake)
            return memo[(i, prev)]

        memo = {}
        return maxPoints(0, -1)
      
  
  ## Top Down (Recursion + Memoization) -> O(n*logn) time, O(n) space ##
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        n = len(nums)

        def maxPoints(i):
            if i == n:
                return 0
            
            if i in memo:
                return memo[i]

            notTake = maxPoints(i+1)
            # if nums[i] is taken and next is nums[i] + 1 then skip the next element
            if i+1 < n and nums[i] + 1 == nums[i+1]:
                take = nums[i] * count[nums[i]] + maxPoints(i+2)
            else:
                take = nums[i] * count[nums[i]] + maxPoints(i+1)
            
            memo[i] = max(take, notTake)
            return memo[i]

        memo = {}
        return maxPoints(0)


  ## Tabulation DP -> O(n*logn) time, O(n) space ##
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        dp = [0]*(n)
        dp[0] = count[nums[0]] * nums[0]
        
        for i in range(1, n):
            notTake = dp[i-1]
            if nums[i] == nums[i-1] + 1:
                take = count[nums[i]] * nums[i] + dp[i-2]
            else:
                take = count[nums[i]] * nums[i] + dp[i-1]
            dp[i] = max(take, notTake)
        
        return dp[-1]


  ## Tabulation (space optimized DP) -> O(n*logn) time, O(1) space ##
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        
        prev1 = 0
        prev2 = 0
        
        for i in range(n):
            notTake = prev1
            if i-1 >= 0 and nums[i] == nums[i-1] + 1:
                take = count[nums[i]] * nums[i] + prev2
            else:
                take = count[nums[i]] * nums[i] + prev1
            curr = max(take, notTake)
            
            prev2, prev1 = prev1, curr
        
        return curr
