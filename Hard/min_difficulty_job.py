class Solution:
  """
  You want to schedule a list of jobs in d days. 
  Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

  You have to finish at least one task every day. 
  The difficulty of a job schedule is the sum of difficulties of each day of the d days. 
  The difficulty of a day is the maximum difficulty of a job done on that day.
  
  You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
  
  Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
  """
    def solve(self, i, d, job, n):
        if i >= n:
            return 0
        if d == 1:
            return max(job[i:n])
        
        if memo[i][d] != -1:
            return memo[i][d]

        ans = 1e9
        for j in range(i+1, n):
            ans = min(ans, max(job[i:j]) + self.solve(j, d-1, job, n))

        memo[i][d] = ans
        return ans
        
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        global memo
        memo = [[-1]*(d+1) for _ in range(n+1)]

        return self.solve(0, d, jobDifficulty, n)
