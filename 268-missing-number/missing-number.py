class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_arr=len(nums)
        expected_sum = (len_arr * (len_arr + 1)) / 2
        num_sum = sum(nums)
        return expected_sum-num_sum

        
        