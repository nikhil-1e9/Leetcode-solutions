from collections import Counter
class Solution:
  """
  Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
  """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      ## One liner
        return len(set(Counter(arr).values())) == len(set(arr))
      ## More readable
        count = Counter(arr)
        unique = count.values()
        return len(set(unique)) == len(unique)
