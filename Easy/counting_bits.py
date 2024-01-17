class Solution:
  """
  Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
  """
    # Function to count set bits in binary of n
    def countOnes(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
      
    ## Naive approach
    ## O(nlogn) time solution
    def countBits(self, n: int) -> List[int]:
        return [self.countOnes(i) for i in range(n+1)]

    ## Optimized approach
    ## Recursive memoization DP O(n) time O(n) space
    def solve(self, n, ans):
        if n == 0:
            return 0
        if ans[n] == 0:
            ans[n] = self.solve(n//2, ans) + n%2
        return ans[n]

    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            self.solve(i, ans//2) + i%2
        return ans

    ## Optimized approach
    ## Iterative DP approach
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = ans[i//2] + i%2
        return ans
