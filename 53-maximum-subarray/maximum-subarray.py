class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        i = 0
        curr_sum = 0

        while i<len(nums):
            new_sum = curr_sum + nums[i]
            max_sum = max(max_sum, new_sum)
            if new_sum > 0:                
                curr_sum = new_sum
            
            else:        
                curr_sum = 0

            i += 1
        
        return max_sum
            

            

            
        