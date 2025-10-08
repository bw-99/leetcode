from typing import List
from collections import deque

class Solution:
    move_lst = [[0, 1],[0, -1],[1, 0],[-1, 0]]

    def bfs(self, row, col):
        queue = deque([(row, col)])
        cells = []                 # 이번 컴포넌트의 모든 좌표
        is_not_surrounded = True

        self.visited[row][col] = True

        while queue:
            r, c = queue.popleft()
            cells.append((r, c))

            for dr, dc in self.move_lst:
                nr, nc = r + dr, c + dc

                # 경계를 벗어나면 둘러싸이지 않음
                if not (0 <= nr < self.num_row and 0 <= nc < self.num_col):
                    is_not_surrounded = False
                    continue

                if self.board[nr][nc] == "O" and not self.visited[nr][nc]:
                    self.visited[nr][nc] = True
                    queue.append((nr, nc))

        # 새 보드로 교체하지 말고, 원래 보드에 직접 반영
        if is_not_surrounded:
            for r, c in cells:
                self.board[r][c] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        self.board = board                 # 원본 객체를 참조만 하고
        self.num_row, self.num_col = len(board), len(board[0])
        self.visited = [[False]*self.num_col for _ in range(self.num_row)]

        for r in range(self.num_row):
            for c in range(self.num_col):
                if self.board[r][c] == "O" and not self.visited[r][c]:
                    self.bfs(r, c)

        # ❌ board = self.board  (필요 없음; 오히려 문제)