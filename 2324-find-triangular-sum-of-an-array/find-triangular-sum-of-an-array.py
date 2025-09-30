class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while(len(nums))>1:
            new_arr=[]
            for i in range(len(nums)-1):
                j=i+1
                sum_of_two=nums[i]+nums[j]
                if sum_of_two>9:
                    sum_of_two=sum_of_two%10
                new_arr.append(sum_of_two)
            nums=new_arr
        return nums[0]

            
        