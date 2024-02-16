class Solution:
  """
  Given an array of integers arr, find the sum of min(b), 
  where b ranges over every (contiguous) subarray of arr. 
  Since the answer may be large, return the answer modulo 10^9 + 7.
  """
  ## ------ Using minimum window of size k ------ ##
    def minSubarrayWindow(self, arr, k):
        n = len(arr)
        ans = 0
        q = deque()

        for i in range(n):
            if q and i-q[0] == k:
                q.popleft()

            while q and arr[i] <= arr[q[-1]]:
                q.pop()
            q.append(i)

            if i >= k-1:
                ans += arr[q[0]]

        return ans

  ## ------------ O(n^2) time, O(n) space --------------
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        n = len(arr)
        ans = 0
        for i in range(n):
            ans += self.minSubarrayWindow(arr, i+1)
        return ans % MOD


  ## ----------- Using monotonic stack ------------- ##
  ## ------------ O(n) time, O(n) space --------------
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9+7
        ans = 0
        stack = [-1]
        arr += [0]
        n = len(arr)
        
        for i in range(n):
            while arr[i] < arr[stack[-1]]:
                index = stack.pop()
                # Smaller element on the left of current index
                leftSmaller = stack[-1]
                # Smaller element on the right of current index
                rightSmaller = i
                # Differences between the current and left, right
                leftDiff = index - leftSmaller
                rightDiff = rightSmaller - index
                # Add the number of subarrays * value to the answer
                ans += leftDiff * rightDiff * arr[index]
            
            stack.append(i)
        
        return ans % MOD
