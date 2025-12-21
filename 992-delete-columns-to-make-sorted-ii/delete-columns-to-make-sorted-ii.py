class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)      # Number of rows
        m = len(strs[0])   # Number of columns

        # is_sorted[i] tracks the relationship between row i and row i+1
        # False = they are currently TIED (identical prefixes)
        # True  = they are STRICTLY SORTED (row i < row i+1)
        is_sorted = [False] * (n - 1)
        del_cnt = 0

        # Iterate through each column from left to right
        for col in range(m):
            is_col_bad = False

            # CHECK PHASE: Does this column break any existing ties?
            for row in range(n - 1):
                # We only check pairs that are NOT yet strictly sorted
                if not is_sorted[row]:
                    # If the top character is greater than bottom, order is invalid
                    if strs[row][col] > strs[row + 1][col]:
                        is_col_bad = True
                        break # Optimization: Stop checking this column immediately

            # DECISION PHASE
            if is_col_bad:
                # If the column is invalid, we must "delete" it
                del_cnt += 1
            else:
                # If we keep the column, we must update the state of our rows
                for i in range(n - 1):
                    # If they were tied, but this column breaks the tie (top < bottom)...
                    if not is_sorted[i] and strs[i][col] < strs[i + 1][col]:
                        is_sorted[i] = True # Mark as strictly sorted (SAFE)

        return del_cnt