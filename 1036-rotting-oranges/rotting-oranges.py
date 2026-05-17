import queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time =0
        rows = len(grid)
        columns = len(grid[0])
        queues = queue.deque()
        rotten = 0
        good = 0
        visited = set()

        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    good+=1
                elif grid[i][j]==2:
                    rotten+=1
                    queues.append((i,j))

        while queues and good>0:
            time+=1
            for iter in range(len(queues)):
                row,column = queues.popleft()
                dim = [(0,1),(0,-1),(1,0),(-1,0)]
                for r, c in dim:
                    neigc = column+c
                    neigr = row+r
                    if 0<=neigc < columns and 0<=neigr<rows and grid[neigr][neigc] == 1:
                        visited.add((row,column))
                        grid[neigr][neigc]=2
                        queues.append([neigr,neigc])
                        good-=1
                        rotten+=1
        return -1 if good>0 else time



        