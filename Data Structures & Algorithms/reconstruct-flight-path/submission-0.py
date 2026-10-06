class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, destination in tickets:
            heapq.heappush(graph[source], destination)
        
        result = []
        def dfs(node):
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            result.append(node)
        dfs('JFK')
        return result[::-1]
        