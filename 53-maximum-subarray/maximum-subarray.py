class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum  = float('-inf')
        
        sum_ = 0

        for n in nums:
            sum_ = max(n, sum_ + n)
            

            max_sum = max(max_sum, sum_)

        return max_sum