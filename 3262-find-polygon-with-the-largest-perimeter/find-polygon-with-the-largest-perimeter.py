class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return -1
        maximum=max(nums)
        print(maximum)
        nums.remove(maximum)
        while(maximum>=sum(nums)):
            if len(nums)==0:
                return -1
            print(nums)
            maximum=max(nums)
            nums.remove(maximum)
        return sum(nums)+maximum


        