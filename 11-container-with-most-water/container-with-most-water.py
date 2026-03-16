class Solution:
    def maxArea(self, height: List[int]) -> int:
        store=0
        l=len(height)
        i=0
        j=l-1
        while i<j:
            if min(height[i],height[j])*(j-i)>store:
                store=min(height[i],height[j])*(j-i)
                
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return store


        