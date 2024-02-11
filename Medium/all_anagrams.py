class Solution:
  """
  Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
  You may return the answer in any order.

  An Anagram is a word or phrase formed by rearranging the letters 
  of a different word or phrase, typically using all the original letters exactly once.
  """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Make arrays for count chars in s and p
        arr_s = [0]*26
        arr_p = [0]*26
        ans = []
        # Assign 2 pointers to keep track of current window
        l, r = 0, 0
        
        while r < len(s):
            # Push elements until full length of p is tracked
            if r < len(p):
                arr_p[ord(p[r])-ord('a')] += 1

            # Push end char of window to arr
            arr_s[ord(s[r])-ord('a')] += 1

            # If window length equals len(p)
            if r-l+1 == len(p):
                # If all character frequencies are equal in both arr
                if arr_s == arr_p:
                    ans.append(l)
                
                # Decrease count of char which is not part of window
                arr_s[ord(s[l])-ord('a')] -= 1
                l += 1

            r += 1

        return ans
