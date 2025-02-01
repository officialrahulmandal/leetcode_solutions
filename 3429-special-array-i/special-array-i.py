class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last=0
        if len(nums)==1:
            return True
        for n in nums:
            if last==0:
                last=n
            elif last%2==n%2:
                return False
            else:
                last=n
        return True




        