class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==0:
            return
        elif len(nums)==1:
            return nums[0]
        max_t=0
        current_total = 0
        start=0
        last=0
        for n in nums:
            if n>last:
                current_total+=n
                if max_t<current_total:
                    max_t=current_total
                last=n
            else:
                current_total=n
                last=n
        return max_t
