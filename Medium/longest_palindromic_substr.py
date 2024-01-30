class Solution:
  """
  Given a string s, return the longest palindromic substring in s.
  """
    def isPalindrome(self, s):
        return s == s[::-1]

  # -------------- Brute force solution ---------------
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        ans = ""
      
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                string = s[i:j]
                
                if self.isPalindrome(string) and maxLen < len(string):
                    ans = string
                    maxLen = len(string)
                  
        return ans
      

    def palindromeFromMid(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

  # ---------- Optimal solution -------------
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        ans = ""
      
        for i in range(len(s)):
            string = self.palindromeFromMid(s, i, i)
            if maxLen < len(string):
                ans = string
                maxLen = len(string)
            
            string = self.palindromeFromMid(s, i, i+1)
            if maxLen < len(string):
                ans = string
                maxLen = len(string)

        return ans
