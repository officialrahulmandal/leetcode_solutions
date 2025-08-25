class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        maxKey = len(mat) + len(mat[0]) - 2
        KEY = [[] for _ in range(maxKey + 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp = KEY[i + j]
                tmp.append([mat[i][j], len(mat[0]) * i + j])

        res = []

        for k in range(maxKey + 1):
            v = KEY[k]
            if k & 1:
                for i in range(len(v)):
                    res.append(v[i][0])  # keep order
            else:
                for i in range(len(v) - 1, -1, -1):
                    res.append(v[i][0])  # reverse order

        return res