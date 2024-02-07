class Solution:
  """
  Given an array of distinct integers candidates and a target integer target, 
  return a list of all unique combinations of candidates where the chosen numbers sum to target. 
  You may return the combinations in any order.

  The same number may be chosen from candidates an unlimited number of times. 
  Two combinations are unique if the frequency of at least one of the chosen numbers is different.
  
  The test cases are generated such that the number of unique combinations 
  that sum up to target is less than 150 combinations for the given input.
  """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        out = []

        def solve(i, res, ans):
            if i >= n:
                return
            if res < 0:
                return
            if res == 0:
                out.append(ans[:])
                return
            
            ans.append(candidates[i])
            solve(i, res-candidates[i], ans)
            ans.pop()
            solve(i+1, res, ans)

        solve(0, target, [])
        return out
