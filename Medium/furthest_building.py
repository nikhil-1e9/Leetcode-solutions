class Solution:
  """
  You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

  You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
  
  While moving from building i to building i+1 (0-indexed),
  
  - If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
  - If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
  - Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
  """
  ## ----------- Dynamic Programming solution (Memory limit exceeded) ----------- ##
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        def spiderMan(i, brick, ladder):
            if i == n-1:
                return i
            
            if (i, brick, ladder) in memo:
                return memo[(i, brick, ladder)]

            if heights[i] < heights[i+1]:
                diff = heights[i+1] - heights[i]
                ans = i
                if brick >= diff:
                    ans = max(ans, spiderMan(i+1, brick-diff, ladder))
                if ladder >= 1:
                    ans = max(ans, spiderMan(i+1, brick, ladder-1))
            else:
                ans = spiderMan(i+1, brick, ladder)

            memo[(i, brick, ladder)] = ans
            return ans
            
        memo = {}
        return spiderMan(0, bricks, ladders)


  ## ----------- Optimal solution (greedy) using Max Heap -> O(nlogn) time ----------- ##
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        maxHeap = []

        for i in range(n-1):
            if heights[i] >= heights[i+1]:
                continue
            
            diff = heights[i+1] - heights[i]
            bricks -= diff
            heappush(maxHeap, -diff)

            if bricks < 0:
                bricks += -heappop(maxHeap)
                if ladders:
                    ladders -= 1
                else:
                    return i
            
        return n-1
