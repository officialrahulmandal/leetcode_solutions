class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        @cache
        def solve(i, j, curr):
            if i>=len(grid) or j>=len(grid[0]) or curr<0: return False
            curr += 1 if grid[i][j]=='(' else -1
            if i==len(grid)-1 and j==len(grid[0])-1: return curr==0
            return solve(i+1, j, curr) or solve(i, j+1, curr)
        return solve(0, 0, 0)