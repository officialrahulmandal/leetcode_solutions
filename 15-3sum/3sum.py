class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                value = nums[i] + nums[j] + nums[k]
                if value == 0:
                    results.append([nums[i] , nums[j] , nums[k]])
                    j+=1
                    while j+1<len(nums) and nums[j] == nums[j-1]:
                        j+=1
                elif value > 0:
                    k-=1
                else:
                    j+=1
                
        return results
        