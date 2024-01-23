class Solution:
  """
  Given an integer array nums of unique elements, return all possible subsets (the power set).

  The solution set must not contain duplicate subsets. Return the solution in any order.
  """
    # --------------- Recursive solution -------------------
    def generateSubsets(self, arr, i, n, ans):
        # Base case
        if i == n:
            out.append(ans[:])
            return 
        
        # Element included case
        ans.append(arr[i])
        self.generateSubsets(arr, i+1, n, ans)
        # Backtrack and delete the included element to return to previous state
        ans.pop()
        # Element not included case
        self.generateSubsets(arr, i+1, n, ans)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        global out
        out = []
        self.generateSubsets(nums, 0, len(nums), [])
        return out



    # ------------ Iterative solution -----------------
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = [[]]
        for num in nums:
            out += [x+[num] for x in out]
        return out
