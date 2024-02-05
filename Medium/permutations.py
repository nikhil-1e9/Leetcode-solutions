class Solution:
  """
  Given an array nums of distinct integers, return all the possible permutations. 
  You can return the answer in any order.
  """
    def getPermutations(self, arr, i, n):
        if i == n:
            ans.append(arr[:])
            return 

        for j in range(i,n):
            arr[i], arr[j] = arr[j], arr[i]
            self.getPermutations(arr, i+1, n)
            arr[i], arr[j] = arr[j], arr[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        global ans
        ans = []
        self.getPermutations(nums, 0, len(nums))
        return ans
