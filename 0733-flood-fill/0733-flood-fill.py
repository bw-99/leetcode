class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        visited = [[False]*len(image[0]) for _ in range(len(image))]
        move_lst = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        start_color = image[sr][sc]

        def dfs(row, col):
            nonlocal color

            if visited[row][col]:
                return
            
            visited[row][col] = True
            image[row][col] = color

            for drow, dcol in move_lst:
                nrow, ncol = row+drow, col+dcol

                if (0<=nrow<len(image)) and (0<=ncol<len(image[0])) and (image[nrow][ncol] == start_color):
                    dfs(nrow, ncol)
        dfs(sr, sc)
        return image
        