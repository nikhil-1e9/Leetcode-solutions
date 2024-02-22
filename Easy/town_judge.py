class Solution:
  """
  In a town, there are n people labeled from 1 to n. 
  There is a rumor that one of these people is secretly the town judge.

  If the town judge exists, then:
  
  - The town judge trusts nobody.
  - Everybody (except for the town judge) trusts the town judge.
  - There is exactly one person that satisfies properties 1 and 2.
  
  You are given an array trust where trust[i] = [ai, bi] representing 
  that the person labeled ai trusts the person labeled bi. 
  If a trust relationship does not exist in trust array, 
  then such a trust relationship does not exist.
  
  Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
  """
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return n if n == 1 else -1

        judge = defaultdict(int)

        for x, y in trust:
            judge[x] -= 1
            judge[y] += 1
        
        for j in judge:
            if judge[j] == n-1:
                return j
        
        return -1
