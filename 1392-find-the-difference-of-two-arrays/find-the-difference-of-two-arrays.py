class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq1={}
        freq2={}
        for n1 in nums1:
            if n1 in freq1:
                continue
            else:
                freq1[n1]=1
        
        for n2 in nums2:
            if n2 in freq2:
                continue
            else:
                freq2[n2]=1
                
        r1=[]
        for n1 in freq1:
            if n1 in freq2:
                continue
            else:
                r1.append(n1)

        r2=[]
        for n2 in freq2:
            if n2 in freq1:
                continue
            else:
                r2.append(n2)
        return [r1,r2]
        