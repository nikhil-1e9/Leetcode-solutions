class Solution:
  """
  We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

  You're given the startTime, endTime and profit arrays, 
  return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
  
  If you choose a job that ends at time X you will be able to start another job that starts at time X.
  """
  # Find next index of job that has endTime >= startTime of included job
    def nextIndex(self, arr, i, n):
        left = i
        right = n-1
        res = n

        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid][0] >= arr[i][1]:
                res = mid
                right = mid-1
            else:
                left = mid+1
        
        return res

    def solve(self, time, i, n):
        ## Base case
        if i >= n:
            return 0
          
        # If answer already calculated then just return it
        if memo[i] != -1:
            return memo[i]

        # Linear search to find next valid job index
        # j = i
        # while j < n and time[i][1] > time[j][0]:
        #     j += 1
      
      # Use binary search instead of linear search
        j = self.nextIndex(time, i, n)

        memo[i] = max(time[i][2] + self.solve(time, j, n), self.solve(time, i+1, n))
        return memo[i]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)

      # Sort the combined list in order of start times of jobs
        time = list(zip(startTime, endTime, profit))
        time.sort()

      # Cache for storing the states
        global memo
        memo = [-1]*n
        
        return self.solve(time, 0, n)
