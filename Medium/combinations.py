class Solution:
  """
  Given two integers n and k, return all possible 
  combinations of k numbers chosen from the range [1, n].

  You may return the answer in any order.
  """
    def combine(self, n: int, k: int) -> List[List[int]]:
        def nCk(i, ans):
            if len(ans) == k:
                res.append(ans[:])
                return 
            if i > n:
                return
            
            ans.append(i)
            nCk(i+1, ans)
            ans.pop()
            nCk(i+1, ans)
        
        res = []
        nCk(1, [])
        return res
