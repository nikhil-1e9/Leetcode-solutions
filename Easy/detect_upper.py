class Solution:
  """
  We define the usage of capitals in a word to be right when one of the following cases holds:

  All letters in this word are capitals, like "USA".
  All letters in this word are not capitals, like "leetcode".
  Only the first letter in this word is capital, like "Google".
  
  Given a string word, return true if the usage of capitals in it is right.
  """
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        count_upper = 0
        for w in word:
            count_upper += w.isupper()
        
        if count_upper==len(word) or count_upper==1 and word[0].isupper() or count_upper==0:
            return True
        return False

    def detectCapitalUse(self, word: str) -> bool:
      ## One liner
        return word.isupper() or word.islower() or word.istitle()
