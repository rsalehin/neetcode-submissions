class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def find_indegree(graph):
            indegree = {node : 0 for node in graph}
            for node in graph:
                for neighbor in graph[node]:
                    indegree[neighbor] += 1
            return indegree

        def create_graph(words):
            graph = {c : set() for word in words for c in word}

            for i in range(len(words) - 1):
                word1, word2 = words[i], words[i + 1]
                minLen = min(len(word1), len(word2))
                if len(word1) > len(word2) and word1[: minLen] == word2[: minLen]:
                    return ""
                for j in range(minLen):
                    if word1[j] != word2[j]:
                        if word2[j] not in graph[word1[j]]:
                            graph[word1[j]].add(word2[j])
                        break
            return graph

        def topological_sort(graph):
            indegree = find_indegree(graph)
            q = deque()
            for node in indegree:
                if indegree[node] == 0:
                    q.append(node)
            result = []
            while q:
                ch = q.popleft()
                result.append(ch)

                for neighbor in graph[ch]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
            if len(result) != len(indegree): 
                return ""
            return "".join(result)
        return topological_sort(create_graph(words))
        