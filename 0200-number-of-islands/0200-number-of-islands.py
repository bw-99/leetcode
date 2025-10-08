class Solution:
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def dfs(self, row, col):
        self.visited[row][col] = True

        for drow, dcol in self.move:
            nrow, ncol = row+drow, col+dcol
            if not (0<=nrow<len(self.grid) and 0<=ncol<len(self.grid[0])):
                continue
            if not self.visited[nrow][ncol] and self.grid[nrow][ncol] == "1":
                self.dfs(nrow, ncol)

        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.visited = [[False] * len(self.grid[0]) for _ in range(len(self.grid))]

        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == "1" and not self.visited[row][col]:
                    self.dfs(row, col)
                    count+=1        
        return count