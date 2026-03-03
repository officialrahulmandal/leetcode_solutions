class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum=0
        i=0
        zero=0
        for j in range(len(nums)):
            if nums[j]==0:
                zero+=1
            while zero>1:
                if nums[i]==0:
                    zero-=1
                i+=1
            maximum = max(maximum, j-i)
        return maximum

        