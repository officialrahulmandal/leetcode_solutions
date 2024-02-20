class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_arr=len(nums)
        i=0
        while(i<len_arr):
            if i!=nums[i]:
                return i
                break
            i+=1
        return i

        
        