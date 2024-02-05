class Solution:
  """
  Given two strings s and t of lengths m and n respectively, return the minimum window substring
  of s such that every character in t (including duplicates) is included in the window. 
  If there is no such substring, return the empty string "".

  The testcases will be generated such that the answer is unique.
  """
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        s_dict = defaultdict(int)
        t_dict = Counter(t)
        need = len(t_dict)
        have = 0
        l = 0
        i, j = -1, -1
        minLen = 1e6

        for r in range(len(s)):
            if s[r] in t_dict:
                s_dict[s[r]] += 1
                if s_dict[s[r]] == t_dict[s[r]]:
                    have += 1
            
            while have == need:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    i, j = l, r
                
                if s[l] in t_dict:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] < t_dict[s[l]]:
                        have -= 1
                
                l += 1
        
        return s[i:j+1]
