class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid)
        minHeap = [(grid[0][0], 0, 0)] # time, r, c
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        visited.add((0, 0))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r == rows-1 and c == cols-1):
                    return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr <0 or nr>=rows or nc < 0 or nc >= cols or (nr, nc) in visited):
                    continue
                visited.add((nr, nc))
                heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))
        
        


        