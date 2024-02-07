class Solution:
  """
  Given a string s, sort it in decreasing order based on the frequency of the characters. 
  The frequency of a character is the number of times it appears in the string.

  Return the sorted string. If there are multiple answers, return any of them.
  """
    def frequencySort(self, s: str) -> str:
        ans = ""
        freq = Counter(s)
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        for char, val in freq:
            ans += char * val    

        return ans
