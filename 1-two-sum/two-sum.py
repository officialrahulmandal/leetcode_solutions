class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        store={}
        for i in range(l):
            if target-nums[i] in store:
                return [store[target-nums[i]],i]
            else:
                store[nums[i]]=i
        