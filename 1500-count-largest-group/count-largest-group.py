class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        n = str(n)
        digits = len(n)
        dp = {0:[1], 1: [1 for _ in range(10)]} ## base case
        for i in range(2, digits):
            dp[i] = [0 for _ in range(9*i+1)]
            for curr_digit in range(10):
                for prev_digit_sum, cnt in enumerate(dp[i-1]):
                    dp[i][prev_digit_sum + curr_digit] += cnt
        
        dp[digits] = [0 for _ in range(9*digits+1)]
        digit_sum = 0
        while digits > 0:
            for curr_digit in range(10):
                if curr_digit == int(n[len(n) - digits]):
                    digit_sum += curr_digit
                    break
                
                for prev_digit_sum, cnt in enumerate(dp[digits-1]):
                    dp[len(n)][digit_sum + curr_digit + prev_digit_sum] += cnt
            digits -= 1
        dp[len(n)][digit_sum] += 1

        return Counter(dp[len(n)])[max(dp[len(n)])]
                