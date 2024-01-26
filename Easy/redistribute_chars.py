class Solution:
  """
  You are given an array of strings words (0-indexed).

  In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, 
  and move any character from words[i] to any position in words[j].

  Return true if you can make every string in words equal using any number of operations, and false otherwise.
  """
    def makeEqual(self, words: List[str]) -> bool:
        arr = [0]*26
        n = len(words)
        
        for word in words:
            for char in word:
                idx = ord(char) - ord('a')
                arr[idx] += 1
                
        for x in arr:
            if x % n:
                return False
        return True
