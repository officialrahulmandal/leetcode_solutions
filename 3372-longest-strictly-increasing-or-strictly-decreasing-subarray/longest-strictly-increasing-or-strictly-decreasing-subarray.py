class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        start=None
        count=1
        max=0
        dec=False
        inc=False
        n = len(nums)
        for i in nums:
            if start is None:
                start=i
                
            elif start<i and inc is False and dec is False:
                inc=True
                count+=1
                
            elif start>i and inc is False and dec is False:
                dec=True
                count+=1
                
            elif start>i and inc is True:
                inc=False
                dec=True
                count=2
            elif start<i and dec is True:
                dec=False
                inc=True
                count=2
            elif start<i and inc is True:
                count+=1
                
            elif start>i and dec is True:
                count+=1
                
            else:
                count=1
                inc=False
                dec=False

            if max<count:
                    max=count
            start=i
            
        return max

        