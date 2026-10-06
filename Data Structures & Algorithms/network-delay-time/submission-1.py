class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Shortest Path Fastest 
        adj = defaultdict(list)
        for u, w, t in times:
            adj[u].append((w, t))
        # Set up distance
        distance = [math.inf] * (n + 1)
        # Set the start node distance to 0
        distance[k] = 0
        #Set up queue
        q = deque()
        q.append(k)
        # set up visited set
        in_queue = [False] * (n + 1)
        in_queue[k] = True 

        while q:
            node = q.popleft()
            in_queue[node] = False
            for neighbor, weight in adj[node]:
                if distance[node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[node] + weight
                    if not in_queue[neighbor]:
                        q.append(neighbor)
                        in_queue[neighbor] = True
        max_time = max(distance[1:])
        return max_time if max_time < math.inf else -1

        