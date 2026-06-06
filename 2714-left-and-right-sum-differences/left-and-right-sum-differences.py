class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix_sum = [0] * len(nums)
        postfix_sum = [0] * len(nums)

        for i in range(1,len(nums)):
            prefix_sum[i] = prefix_sum[i-1]+nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            postfix_sum[i] = postfix_sum[i+1]+nums[i+1]

        for i in range(len(nums)):
            nums[i] = abs(prefix_sum[i] - postfix_sum[i])

        return nums
            

        