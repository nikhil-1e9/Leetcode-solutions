class Solution:
  """
  Given a string containing digits from 2-9 inclusive, 
  return all possible letter combinations that the number could represent. 
  Return the answer in any order.

  A mapping of digits to letters (just like on the telephone buttons) is given below. 
  Note that 1 does not map to any letters.
  """
  ## ------------------ Recursive approach -------------------
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        n = len(digits)
        
        def combine(i, letters):
            if i == n:
                if letters:
                    # res.append(letters)
                    res.append("".join(letters))
                return 
            
            digit = digits[i]
            for char in mapping[digit]:
                # combine(i+1, letters+char)
                letters.append(char)
                combine(i+1, letters)
                letters.pop()
                
            
        res = []
        combine(0, [])
        return res


  ## --------------- Iterative approach -----------------
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        n = len(digits)
        if n == 0:
            return None
        
        res = [""]
        for digit in digits:
            tmp = []
            for char in mapping[digit]:
                for i in range(len(res)):
                    tmp.append(res[i]+char)
            res = tmp
        
        return res
