class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2= 0, 0
        for n in nums:
            curr = max(prev1, prev2+n)
            prev1, prev2= curr, prev1

        return max(prev1, prev2)
        