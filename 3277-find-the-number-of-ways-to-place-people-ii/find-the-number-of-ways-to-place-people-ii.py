class Solution:
    def numberOfPairs(self, points):
        n = len(points)
        if n <= 1:
            return 0

        # Coordinate compression
        xs = sorted({x for x, y in points})
        ys = sorted({y for x, y in points})
        x_map = {v: i + 1 for i, v in enumerate(xs)}
        y_map = {v: i + 1 for i, v in enumerate(ys)}

        comp = [(x_map[x], y_map[y]) for x, y in points]
        max_x, max_y = len(xs), len(ys)

        # grid (1-based indexing)
        grid = [[0] * (max_y + 1) for _ in range(max_x + 1)]
        for x, y in comp:
            grid[x][y] += 1

        # 2D prefix sums
        prefix = [[0] * (max_y + 1) for _ in range(max_x + 1)]
        for i in range(1, max_x + 1):
            row_sum = 0
            for j in range(1, max_y + 1):
                row_sum += grid[i][j]
                prefix[i][j] = prefix[i - 1][j] + row_sum

        def rect_sum(x1, y1, x2, y2):
            if x1 > x2 or y1 > y2:
                return 0
            return (prefix[x2][y2]
                    - prefix[x1 - 1][y2]
                    - prefix[x2][y1 - 1]
                    + prefix[x1 - 1][y1 - 1])

        ans = 0
        # Check all ordered pairs (Alice, Bob)
        for i in range(n):
            x1, y1 = comp[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = comp[j]
                # Alice is upper-left and Bob is lower-right
                if x1 <= x2 and y1 >= y2:
                    # if only these two points lie inside/on the rectangle
                    if rect_sum(x1, y2, x2, y1) == 2:
                        ans += 1
        return ans