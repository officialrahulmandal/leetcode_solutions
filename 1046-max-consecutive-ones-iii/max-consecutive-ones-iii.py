class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maximum=0
        i=0
        zero=0
        for j in range(len(nums)):
            if nums[j]==0:
                zero+=1
            while zero>k:
                if nums[i]==0:
                    zero-=1
                i+=1
                
            maximum = max(maximum, j-i+1)
        return maximum
            
            