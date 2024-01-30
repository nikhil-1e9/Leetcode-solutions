class Solution:
  """
  Given an integer array nums, return true if any value appears at least twice in the array, 
  and return false if every element is distinct.
  """
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## Brute Force solution using 2 loops
        ## --------O(n^2) time O(1) space complexity-------
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


    def containsDuplicate(self, nums: List[int]) -> bool:
        ## Sorting the array and looking at adjacent elements
        ## ------O(nlogn) time O(1) space complexity-------
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

      
    def containsDuplicate(self, nums: List[int]) -> bool:  
        ## Using HashSet O(n) time O(n) space complexity
        dup = set()
        for num in nums:
            if num in dup:
                return True
            else:
                dup.add(num)
        return False
