class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        board = [["."]*n for _ in range(n)]
        columns = set()
        pDiagonals = set()
        nDiagonals = set()

        def backtrack(row):
            if row==n:
                r1 = [''.join(ro) for ro in board]
                result.append(r1)
                return

            for c in range(n):
                if c in columns or (row+c) in pDiagonals or (row-c) in nDiagonals:
                    continue

                columns.add(c)
                pDiagonals.add(row+c)
                nDiagonals.add(row-c)

                board[row][c] = "Q"

                backtrack(row+1)

                columns.remove(c)
                pDiagonals.remove(row+c)
                nDiagonals.remove(row-c)
                board[row][c] = "."




        backtrack(0)
        return result
        