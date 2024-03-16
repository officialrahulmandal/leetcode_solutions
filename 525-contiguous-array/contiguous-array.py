class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest_ca = 0
        counter = {}
        total=0
        ca=0
        for num in range(len(nums)):
            if nums[num] == 0:
                total += -1
            elif nums[num] ==1:
                total +=1

            if total == 0:
                ca=num+1
            else:
                if total in counter:
                    ca = num - counter[total]
                else:
                    counter[total] = num
                
            if ca > longest_ca:
                longest_ca = ca

        return longest_ca


            
        