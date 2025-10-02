class Solution:
    d_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def bfs(self, row, col):
        queue = [(row, col)]
        while queue:
            cur_row, cur_col = queue.pop(0)
            if self.visited[cur_row][cur_col]:
                continue

            self.visited[cur_row][cur_col] = True

            for drow, dcol in self.d_list:
                next_row, next_col = cur_row + drow, cur_col + dcol

                if not (
                    (0<=next_row<len(self.grid)) and 
                    (0<=next_col<len(self.grid[0]))
                ):
                    continue

                if not self.visited[next_row][next_col] and self.grid[next_row][next_col] == "1":
                    queue.append([next_row, next_col])

            

    def numIslands(self, grid: List[List[str]]) -> int:
        num_row, num_col = len(grid), len(grid[0])
        self.visited = [[False] * num_col for _ in range(num_row)]
        self.grid = grid
        count = 0
        
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == "1" and not self.visited[row][col]:
                    self.bfs(row, col)
                    count+=1
        return count