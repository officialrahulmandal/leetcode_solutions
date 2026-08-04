class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count = [1]*len(nums)
        result = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    count[i] = max(count[i],count[j]+1)
                    result=max(result,count[i])
                
        return result


        