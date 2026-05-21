class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0 : -1}
        prefix_sum = 0
        
        
        for i, num in enumerate(nums):
            print(i)
            prefix_sum += num

            reminder = prefix_sum%k
            if reminder not in rem:
                rem[reminder] = i
            elif i-rem[reminder]>=2 :
                return True

            

            
        return False

        