class Solution:
    find = False

    def search(self, row, col, visited, idx, word):
        if self.find:
            return

        visited[row][col] = True

        if len(word) == idx+1:
            self.find = True
            return

        for drow, dcol in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            next_row, next_col = row+drow, col+dcol
            if not (0<=next_row<self.nrow and (0<=next_col<self.ncol)):
                continue
            if visited[next_row][next_col]:
                continue
            
            if self.board[next_row][next_col] == word[idx+1]:
                visited[next_row][next_col] = True
                self.search(next_row, next_col, visited, idx+1, word)
                visited[next_row][next_col] = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.nrow, self.ncol = len(board), len(board[0])

        for row in range(self.nrow):
            for col in range(self.ncol):
                if self.board[row][col] == word[0]:
                    visited = [[False]*self.ncol for _ in range(self.nrow)]
                    self.search(row, col, visited, 0, word)
                    if (self.find):
                        return True
        return False