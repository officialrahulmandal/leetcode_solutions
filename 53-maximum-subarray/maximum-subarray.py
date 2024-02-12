class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        len_arr=len(nums)
        if len_arr==1:
            return nums[0]
        max_sum=float('-inf')
        sum_i=float('-inf')
        while (i<len_arr):
            if sum_i<0:
                sum_i=nums[i]
            else:
                sum_i+=nums[i]
            max_sum=max(max_sum,sum_i)
            i+=1
        return max_sum
            
        