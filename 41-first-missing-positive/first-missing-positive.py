class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        scope = len(nums)
        for i in range(scope):
            val = nums[i]
            if 0<val<=scope:
                continue
            else:
                nums[i]=scope+1

        print(nums)


        #removing out of scope
        for i in range(scope):
            val = abs(nums[i])
            if val>scope:
                continue
            elif nums[val-1]>0:
                nums[val-1]=-(nums[val-1])

        
        for i in range(scope):
            if nums[i]>0:
                return i + 1

        return scope + 1
        