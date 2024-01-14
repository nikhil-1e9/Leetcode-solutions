class Solution:
  """
  Two strings are considered close if you can attain one from the other using the following operations:
  
  Operation 1: Swap any two existing characters.
  For example, abcde -> aecdb
  
  Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
  For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
  
  You can use the operations on either string as many times as necessary.
  Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
  """
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        arr1, arr2 = [0]*26, [0]*26
        for word in word1:
            arr1[ord(word)-ord('a')] += 1
        for word in word2:
            arr2[ord(word)-ord('a')] += 1
        for x,y in zip(arr1,arr2):
            if x == 0 and y != 0:
                return False
            if x != 0 and y == 0:
                return False
        arr1.sort()
        arr2.sort()
        return arr1 == arr2
