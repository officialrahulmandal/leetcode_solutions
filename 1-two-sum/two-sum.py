class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        covered = {}
        for i in range(len(nums)):
            if target-nums[i] in covered:
                return [covered[target-nums[i]], i]
            else:
                covered[nums[i]]= i