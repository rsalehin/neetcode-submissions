class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # SPFA
        prices = [math.inf] * n # Airports labeled from 0 to n-1
        prices[src] =  0
        adj = [[] for i in range(n)]
        for source, destination, weight in flights:
            adj[source].append((destination, weight))
        q = deque()
        q.append((0, src, 0)) # cost, source/start, stops

        while q:
            cost, node, stops = q.popleft()

            if stops > k:
                continue # Don't include the airport if its stop is greater than k. 
            for neighbor, weight in adj[node]:
                nextCost = cost + weight
                if nextCost < prices[neighbor]:
                    prices[neighbor] = nextCost
                    q.append((nextCost, neighbor, stops + 1)) 
        return prices[dst] if prices[dst] < math.inf else -1