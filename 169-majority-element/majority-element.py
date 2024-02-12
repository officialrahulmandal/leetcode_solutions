class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum=float('-inf')
        if len(nums)<=1:
            return nums[0]
        count={}
        element=''
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        print(count)
        for key,value in count.items():
            if value>maximum:
                print(value,maximum)
                maximum=value
                element=key
        return element
        