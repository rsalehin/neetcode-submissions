class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # It's a variant of total islands. While calling the bfs, we also count the 
        # the number of squares in each island. Then while using the for loop, use
        # max_island = 0 and max_island = max(max_island, current_island)
        # Usual setup: length, visited, bfs
        num_row, num_col = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            num_squares = 1
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >=0 and nr < num_row and nc >= 0 and nc < num_col and grid[nr][nc] == 1 and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        num_squares += 1
            return num_squares
        
        max_island = 0
        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_island = max(max_island, bfs(i, j))
        return max_island

        