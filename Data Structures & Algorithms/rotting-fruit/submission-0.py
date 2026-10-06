class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi-source bfs problem
        # Need to find the number of fresh fruits and rotten fruits

        fresh = 0
        time = 0
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_row = len(grid)
        num_col = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        while fresh > 0 and q:

            for _ in range(len(q)):
                r , c =q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0<=nr< num_row and 0<=nc <num_col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        