class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(row, column):
            if grid[row][column] == "1":
                grid[row][column] = "0"
                for r, c in directions:
                    new_r=row+r
                    new_c=column+c
                    if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]):
                        dfs(new_r, new_c)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    islands+=1
        return islands


        