class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        len_arr=len(nums)
        i=0
        j=0
        max_sum=-99999
        sum=0
        while(j<len_arr):
            
            sum+=nums[j]
            #print(i,j,sum)
            max_sum=max(max_sum,sum)
            if sum<0:
                j+=1
                #j+=1
                sum=0
            else:
                j+=1
            
        return max_sum
        