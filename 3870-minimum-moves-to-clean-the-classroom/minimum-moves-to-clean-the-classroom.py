class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])
        cnt_l, mask = 0, {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'L':
                    mask[(i, j)] = 1 << cnt_l
                    cnt_l += 1
                elif classroom[i][j] == 'S':
                    si, sj = i, j
        clear_all = (1 << cnt_l) - 1
        
        max_energy = [[[-1] * (1 << cnt_l) for _ in range(n)] for m in range(m)]
        que = deque([(si, sj, 0, energy, 0)])
        while que:
            i, j, clear, e, s = que.pop()
            if clear == clear_all:
                return s
            if e > 0:
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n and classroom[ii][jj] != 'X':
                        new_e = energy if classroom[ii][jj] == 'R' else e - 1
                        new_clear =  clear | mask[(ii, jj)] if classroom[ii][jj] == 'L' else clear
                        if new_e > max_energy[ii][jj][new_clear]:
                            max_energy[ii][jj][new_clear] = new_e
                            que.appendleft((ii, jj, new_clear, new_e, s+1))
        return -1