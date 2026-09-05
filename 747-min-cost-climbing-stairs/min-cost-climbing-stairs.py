class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[]
        n=len(cost)
        for i, c in enumerate(cost):
            if len(dp)<2:
                dp.append(c)
            else:
                dp.append(c+min(dp[i-1],dp[i-2]))

        return min(dp[n-1],dp[n-2])
        