class Solution:
  """
  Given two strings s and t, return true if t is an anagram of s, and false otherwise.

  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
  typically using all the original letters exactly once.
  """
    # -------------Using sorting----------------
    def isAnagram(self, s: str, t: str) -> bool:
        # --------- One Liner ---------
        return sorted(s) == sorted(t)


    ## ------------ Using Hashmap --------------
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = defaultdict(int)

        for char1, char2 in zip(s, t):
            count[char1] += 1
            count[char2] -= 1
        
        for val in count.values():
            if val != 0:
                return False
        return True

    
    # ---------- Using character array --------------
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr = [0]*26
        ans = arr.copy()
        
        for char1, char2 in zip(s, t):
            arr[ord(char1)-ord('a')] += 1
            arr[ord(char2)-ord('a')] -= 1
        
        return arr == ans
