class Solution:
  """
  Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
  """
    ## -------- Using ordered dict ------------
    def firstUniqChar(self, s: str) -> int:
        char_dict = OrderedDict()
        for char in s:
            char_dict[char] = char_dict.get(char,0) + 1
        
        for char in char_dict:
            if char_dict[char] == 1:
                return s.index(char)
              
        return -1
      
    ## ---------- Using character array -------------
    def firstUniqChar(self, s: str) -> int:
        arr = [0]*26
        for x in s:
            arr[ord(x)-ord('a')] += 1
          
        for i,x in enumerate(s):
            if arr[ord(x)-ord('a')] == 1:
                return i
              
        return -1

    ## ---------- Simple 3 liner -------------
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
      
