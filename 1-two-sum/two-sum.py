class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements={}
        index=0
        for n in nums:
            if target-n in elements:
                return [index,elements[target-n]]
            elements[n]=index
            index+=1
        #for e in elements:
            
        