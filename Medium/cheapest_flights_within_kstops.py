class Solution:
  """
  There are n cities connected by some number of flights. 
  You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that 
  there is a flight from city fromi to city toi with cost pricei.

  You are also given three integers src, dst, and k, 
  return the cheapest price from src to dst with at most k stops. 
  If there is no such route, return -1.
  """
    def __init__(self):
        self.ans = 1e9

  ## -------------- Depth First Search -------------- ##
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = defaultdict(list)
        for s, d, price in flights:
            adjMap[s].append((d, price))
        
        vis = [0]*100

        def dfs(src, dst, stops, vis, total):
            if stops-1 > k:
                return
            if src == dst:
                self.ans = min(self.ans, total)
                return

            vis[src] = 1
            stops += 1
            
            for d, price in adjMap[src]:
                if not vis[d]:
                    if total + price > self.ans:
                        continue
                    total += price
                    dfs(d, dst, stops, vis, total)
                    total -= price
          
            vis[src] = 0
            stops -= 1
          
        dfs(src, dst, 0, vis, 0)
        
        return self.ans if self.ans != 1e9 else -1


  ## -------------------- Breadth First Search ------------------ ##
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create graph
        adjMap = defaultdict(list)
        for s, d, price in flights:
            adjMap[s].append((d, price))

        # Create queue to store the traversing nodes
        q = deque()
        q.append((src, 0))
        # Create array to keep track of minCost for each location
        minCost = [1e9 for _ in range(n)]
        # Initialize stops to zero
        stops = 0
        
        while q and stops <= k:
            n = len(q)
            for _ in range(n):
                # Get the current city and price from the queue
                city, price = q.popleft()

                # Traverse all neighbouring nodes
                for d, cost in adjMap[city]:
                  # Add the new price if it is lower than the previous value for that city
                    if price + cost < minCost[d]:
                        minCost[d] = price + cost
                        q.append((d, minCost[d]))

          # Increment stops by 1
            stops += 1
        
        ans = minCost[dst]
        return ans if ans != 1e9 else -1
