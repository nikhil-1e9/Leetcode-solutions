class Solution:
  """
  You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
  Return the minimum number of steps to make t an anagram of s.
  An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
  """
    def minSteps(self, s: str, t: str) -> int:
        arr = [0]*26
        for char1, char2 in zip(s,t):
            arr[ord(char1)-ord('a')] += 1
            arr[ord(char2)-ord('a')] -= 1
        ans = 0
        for x in arr:
            ans += abs(x)
        return ans//2
