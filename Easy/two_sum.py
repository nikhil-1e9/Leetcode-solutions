class Solution:
  """
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.

  You can return the answer in any order.
  """
    # Time complexity -> O(n), Space complexity -> O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = {}
        
        for i,num in enumerate(nums):
            if num in ans:
                return [ans[num], i]

            ans[target-num] = i

    # Time complexity -> O(nlogn), Space complexity -> O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = sorted(nums)
        i, j = 0, n-1
        
        while i < j:
            if ans[i] + ans[j] == target:
                idx1 = nums.index(ans[i])
                idx2 = nums.index(ans[j])
                
                if idx1 == idx2:
                    idx2 = n - nums[::-1].index(ans[j]) - 1
                
                return [idx1, idx2]
            
            if ans[i] + ans[j] < target:
                i += 1
            else:
                j -= 1
