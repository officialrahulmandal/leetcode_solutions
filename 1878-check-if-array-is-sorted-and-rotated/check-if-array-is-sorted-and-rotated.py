class Solution:
    def check(self, nums: List[int]) -> bool:
        dip = 0
        prev=nums[-1]
        
        for num in nums:
            if prev>num:
                dip += 1
                if dip > 1:
                    return False
                
            prev = num

        return True
        