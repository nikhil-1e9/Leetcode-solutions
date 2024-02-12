class Solution:
  """
  Write a function to find the longest common prefix string amongst an array of strings.

  If there is no common prefix, return an empty string "".
  """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        
        for char1, char2 in zip(strs[0], strs[-1]):
            if char1 != char2:
                break
            res += char1
        return res
