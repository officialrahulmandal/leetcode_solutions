class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        #variable to maintain last number
        last=0
        #if only one value is present in array
        if len(nums)==1:
            return True
        
        #iteration to go through each element
        for n in nums:
            #to be executed only once to set first value as last number
            if last==0:
                last=n
            # to check whether both last and current number is same(both odd or both even)
            elif last%2==n%2:
                return False
            #if not then continue further by updating current number as last number in last variable
            else:
                last=n
        # if we reach till last without any break that means it's an special array
        return True




        