class Solution:
    def areaOfMaxDiagonal(self, a: List[List[int]]) -> int:
        return max((l*l+w*w,l*w) for l,w in a)[1]