class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns={}
        rows={}
        count=0
        count1=0
        for i in range(len(grid[0])):
            value=[]
            for j in range(len(grid)):
                value.append(grid[i][j])
            
            if tuple(value) in columns:
                columns[tuple(value)]+=1
            else:
                columns[tuple(value)]=1
        for i in range(len(grid[0])):
            value=[]
            for j in range(len(grid)):
                value.append(grid[j][i])
            if tuple(value) in columns:
                count+=columns[tuple(value)]
            if tuple(value) in rows:
                rows[tuple(value)]+=1
            else:
                rows[tuple(value)]=1
        for c in columns:
            if c in rows:
                count1+=rows[c]
        return max(count,count1)
        