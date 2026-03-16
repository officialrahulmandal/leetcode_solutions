class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l=len(nums)
        store=[]
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k=i+1
            j=l-1
            while k<j:
                if nums[i]+nums[k]+nums[j]==0:
                    store.append([nums[i],nums[k],nums[j]])
                    k+=1
                    while nums[k] == nums[k-1] and k < j:
                        k += 1
                elif nums[i]+nums[k]+nums[j]>0:
                    j-=1

                else :
                    k+=1
        return store