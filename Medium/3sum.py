class Solution:
  """
  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

  Notice that the solution set must not contain duplicate triplets.
  """
  # -------------Brute Force solution O(n^3) time -------------
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        ans.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        
        return ans

  # -------------- O(n^2) solution using 3 pointers and set ------------
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()

        for i in range(n):
            j, k = i+1, n-1
            
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.add(tuple(sorted((nums[i], nums[j], nums[k]))))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return ans


  # -------------- O(n^2) solution using 3 pointers (more optimal) ------------
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, n-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1; r -= 1
        
        return res
