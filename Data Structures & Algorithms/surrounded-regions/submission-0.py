class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_row, num_col = len(board), len(board[0])
        directions = [(1, 0), (-1 , 0), (0, 1), (0, -1)]

        def bfs():
            q = deque()
            for r in range(num_row):
                for c in range(num_col):
                    if board[r][c] == 'O' and (r == 0 or r == num_row - 1 or c == 0 or c == num_col - 1):
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0<=nr<num_row and 0<=nc<num_col):
                            q.append((nr, nc))
        bfs()
        for r in range(num_row):
            for c in range(num_col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
        