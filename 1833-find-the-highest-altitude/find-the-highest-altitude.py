class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        g=0
        curr=0
        for i in gain:
            curr=curr+i
            if curr>g:
                g=curr
        return g

        

        