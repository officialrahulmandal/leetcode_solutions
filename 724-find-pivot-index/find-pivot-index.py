class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumarr=[]
        initial=0
        sumarr.append(0)
        for i in range(len(nums)-1,-1,-1):
            initial=initial+nums[i]
            sumarr.insert(0,initial)
            
            
        addition=0
        for i in range(len(nums)):
            if sumarr[i+1]==addition:
                return i
            addition=addition+nums[i]
        
        return -1



        