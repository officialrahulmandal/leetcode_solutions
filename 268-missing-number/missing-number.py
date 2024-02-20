class Solution:
    def missingNumber(self, nums):
        nums.sort()
        # print(nums)
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)

        
        