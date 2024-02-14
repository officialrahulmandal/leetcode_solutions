class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=(float('-inf'),0)
        len_array=len(nums)
        for i in range(len_array):
            if nums[i]>maximum[0]:
                maximum=(nums[i],i)
        return maximum[1]
            
        