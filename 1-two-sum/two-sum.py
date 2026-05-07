class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        l=len(nums)
        for i in range(l):
            if target-nums[i] in store:
                return store[target-nums[i]],i
            else:
                store[nums[i]]=i
        