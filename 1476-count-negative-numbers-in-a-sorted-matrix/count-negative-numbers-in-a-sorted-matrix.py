class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        bin = lambda y: bisect_right(y, .5, key = lambda x: -x)
        return len(grid)*len(grid[0])- sum(map(bin, grid))