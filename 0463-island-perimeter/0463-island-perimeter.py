class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        move_lst = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    tmp_answer = 0
                    for drow, dcol in move_lst:
                        nrow, ncol = row+drow, col+dcol
                        
                        if not ((0<= nrow < len(grid)) and (0<=ncol<len(grid[0]))):
                            tmp_answer+=1
                            continue
                        
                        if grid[nrow][ncol] == 0:
                            tmp_answer+=1
                    answer+=tmp_answer
        return answer
                        
        