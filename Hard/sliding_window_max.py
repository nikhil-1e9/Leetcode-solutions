class Solution:
  """
  You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
  You can only see the k numbers in the window. Each time the sliding window moves right by one position.

  Return the max sliding window.
  """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        n = len(nums)
        q = deque()
        ans = []

        for i in range(n):
            # If the front index is no longer in the window remove it 
            if q and i - q[0] >= k:
                q.popleft()

            # Remove all elements less than the current element from the queue
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            # Add the current element into the queue
            q.append(i)

            # Start adding elements to answer once the first window is processed
            if i >= k-1:
                ans.append(nums[q[0]])

        return ans
