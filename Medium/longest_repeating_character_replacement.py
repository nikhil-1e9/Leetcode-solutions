class Solution:
  """
  You are given a string s and an integer k. 
  You can choose any character of the string and change it to 
  any other uppercase English character. You can perform this operation at most k times.

  Return the length of the longest substring containing the same letter 
  you can get after performing the above operations.
  """
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        l = 0
        ans = 0
        
        for r in range(len(s)):
            char[s[r]] = char.get(s[r], 0) + 1
            # Find most frequent character
            maxChar = max(char, key=char.get)
            window = r-l+1
            
            if window - char[maxChar] <= k:
                ans = max(ans, window)
            else:
                char[s[l]] -= 1
                l += 1
        
        return ans
                
