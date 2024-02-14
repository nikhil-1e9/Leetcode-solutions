class Solution:
  """
  You are given two integer arrays nums1 and nums2. 
  We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

  We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
  
  - nums1[i] == nums2[j], and
  - the line we draw does not intersect any other connecting (non-horizontal) line.
  
  Note that a connecting line cannot intersect even at the endpoints 
  (i.e., each number can only belong to one connecting line).
  
  Return the maximum number of connecting lines we can draw in this way.
  """
  ## -------- Recursion + Memoization -> O(m*n) time, O(m*n) space ---------
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        def LCS(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            if nums1[i] == nums2[j]:
                memo[(i, j)] = 1 + LCS(i+1, j+1)
            else:
                memo[(i, j)] = max(LCS(i, j+1), LCS(i+1, j))
            
            return memo[(i, j)]

        memo = {}
        return LCS(0, 0)


  ## -------------- Iterative DP -> O(m*n) time, O(m*n) space ---------------
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:      
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


  ## ----------- Iterative DP, space optimized-> O(m*n) time, O(n) space ------------
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [0]*(n+1)
        
        for i in range(1, m+1):
            curr = [0]*(n+1)
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev = curr

        return prev[-1]
