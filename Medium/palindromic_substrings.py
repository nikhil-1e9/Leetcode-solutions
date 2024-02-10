class Solution:
  """
  Given a string s, return the number of palindromic substrings in it.

  A string is a palindrome when it reads the same backward as forward.

  A substring is a contiguous sequence of characters within the string.
  """
    ## --- Brute force approach -> O(n^3) time --- ##
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                
                if s[i:j+1] == s[i:j+1][::-1]:
                    palindromes += 1
        
        return palindromes


    ## ------ Optimal approach -> O(n^2) time ------ ##
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def countPalindromes(i, j):
            count = 0
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count
        
        palindromes = 0
        
        for i in range(n):
            even = countPalindromes(i, i+1)
            odd = countPalindromes(i, i)
            palindromes += even + odd
        
        return palindromes
