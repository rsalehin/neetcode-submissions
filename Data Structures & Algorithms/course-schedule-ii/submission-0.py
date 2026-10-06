class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def create_graph(numCourses, prerequisites):
            graph = {i : [] for i in range(numCourses)}
            for child, parent in prerequisites:
                graph[parent].append(child)
            return graph
        
        def find_indegree(graph):
            indegree = {node : 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree
        
        graph = create_graph(numCourses, prerequisites)
        indegree = find_indegree(graph)
        q = deque()
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        finish, result = 0, []
        while q:
            node = q.popleft()
            finish += 1
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        if len(result) != len(indegree):
            return []
        return result if finish == numCourses else []

        