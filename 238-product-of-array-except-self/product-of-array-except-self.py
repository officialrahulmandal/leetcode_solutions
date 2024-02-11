class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_arr=len(nums)
        result=[1]*len_arr
        prefix=1
        for i in range(len_arr):
            result[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len_arr-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]
        return result