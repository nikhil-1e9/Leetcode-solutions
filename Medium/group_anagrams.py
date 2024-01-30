class Solution:
  """
  Given an array of strings strs, group the anagrams together. You can return the answer in any order.

  An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
  typically using all the original letters exactly once.
  """
  #-------- Using simple dictionary ------------
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for s in strs:
            x = "".join(sorted(s))
            if x not in str_dict:
                str_dict[x] = []
            str_dict[x].append(s)

        return list(str_dict.values())

  # ----------- Using defaultdict -----------------
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
      
        str_dict = defaultdict(list) # creates dict with values as list 
        for s in strs:
            x = "".join(sorted(s))
            str_dict[x].append(s)

        return list(str_dict.values())
