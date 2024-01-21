class Solution:
  """
  Given an array of integers arr, sort the array by performing a series of pancake flips.
  In one pancake flip we do the following steps:

  Choose an integer k where 1 <= k <= arr.length.
  Reverse the sub-array arr[0...k-1] (0-indexed).
  
  For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, 
  we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.
  
  Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. 
  Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
  """
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []

        for i in range(n-1,-1,-1):
            maxIndex = arr.index(i+1)
            ans.append(maxIndex+1)
            arr = arr[:maxIndex+1][::-1] + arr[maxIndex+1:]
            ans.append(i+1)
            arr = arr[:i+1][::-1] + arr[i+1:]
            
        return ans
