class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        len_arr=len(nums)
        j=0
        max_sum=float('-inf')
        sum=0
        while(j<len_arr):
            
            sum+=nums[j]
            max_sum=max(max_sum,sum)
            if sum<0:
                sum=0
            j+=1
            
        return max_sum
        