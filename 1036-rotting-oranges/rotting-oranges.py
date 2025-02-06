from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh,time=0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i,j])

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh>0:
            for i in range(len(q)):
                c,r = q.popleft()
                for dc,dr in directions:
                    x,y=c+dc,r+dr
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        fresh -= 1
                    # grid[x][y]=2
                    # q.append([x,y])
                    # fresh-=1
            time+=1
        return time if fresh==0 else -1


        