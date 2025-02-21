class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sp=0
        curr=0
        sum=0
        final_sum=-99999
        while curr<=(len(nums)-1):
            sum=sum+nums[curr]
            if sum>final_sum:
                final_sum=sum
            if sum<=0:
                #sp=curr
                sum=0
            curr+=1
        return final_sum
                

            


        