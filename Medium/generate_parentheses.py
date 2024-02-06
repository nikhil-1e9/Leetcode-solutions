class Solution:
  """
  Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
  """
    def solve(self, left, right, n, ans):
        if len(ans) == n*2:
            out.append(ans)
            return 

        if left < n:
            self.solve(left+1, right, n, ans+'(')
        
        if right < left:
            self.solve(left, right+1, n, ans+')')
        
    def generateParenthesis(self, n: int) -> List[str]:
        global out
        out = []
        
        self.solve(0, 0, n, '')
        return out
