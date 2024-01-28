class Solution:
  """
  Given a string s, find the length of the longest substring without repeating characters.
  """
  # --------- Using set ----------------
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        maxLen = 0
        start, end = 0, 0
        
        while end < len(s):
            if len(s[start:end+1]) == len(set(s[start:end+1])):
                count[s[end]] = end
                curLen = end - start + 1
                maxLen = max(maxLen, curLen)
                end += 1
            else:
                start = count[s[end]] + 1
        
        return maxLen

  # ------------- Using hashmap alone ----------------
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        maxLen = 0
        start, end = 0, 0
        
        while end < len(s):
            if s[end] not in count or count[s[end]] < start:
                count[s[end]] = end
                curLen = end - start + 1
                maxLen = max(maxLen, curLen)
                end += 1
            else:
                start = count[s[end]] + 1
                count[s[end]] = end
                end += 1
        
        return maxLen
