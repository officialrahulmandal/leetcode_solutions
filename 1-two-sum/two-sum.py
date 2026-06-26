class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            if store.get(target - nums[i],float(-inf)) != float(-inf):
                return [store.get(target - nums[i]),i]
            else:
                store[nums[i]] = i
            
        return -1