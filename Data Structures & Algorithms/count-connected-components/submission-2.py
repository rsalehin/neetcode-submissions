class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        visited = [False] * n 
        num_connected = 0
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(component):
            visited[component] = True
            for neighbor in adj_list[component]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        for component in range(n):
            if not visited[component]:
                dfs(component)
                num_connected += 1
        return num_connected

        