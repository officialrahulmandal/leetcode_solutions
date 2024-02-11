class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique=set()
        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        return False
        