class Solution:
  """
  Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. 
  If there is no such substring return -1.

  A substring is a contiguous sequence of characters within a string.
  """
    # ------------- Brute Force solution O(n^2) time O(1) space -----------------
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLen = -1
        
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    maxLen = max(maxLen, j-i-1)
        
        return maxLen

    
    # -------------- Optimized approach O(n) time O(1) space ----------------
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        arr1 = [-1]*26
        arr2 = [-1]*26
        
        for i, char in enumerate(s):
            idx = ord(char)-ord('a')
            if arr1[idx] != -1:
                arr2[idx] = i
            else:
                arr1[idx] = i
              
        maxLen = -1
        for i, j in zip(arr1, arr2):
            maxLen = max(maxLen, j-i-1)
        
        return maxLen
