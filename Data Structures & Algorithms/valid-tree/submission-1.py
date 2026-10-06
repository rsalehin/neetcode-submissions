class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n 
        self.count = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False 
        if self.rank[root_x]  > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x]  < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] +=1
        self.count -= 1 
        return True 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Let's use UnionFind. The idea is, given number of nodes and edges, union all the nodes. 
        # While unioning, if any two nodes already share a root, then unioning them means cycle. 
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for x, y in edges:
            if not dsu.union(x, y):
                return False 
        return dsu.count == 1