class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        n=len(nums)
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for key,value in count.items():
            div=n//3
            if (value>div):
                result.append(key)
        return result
        