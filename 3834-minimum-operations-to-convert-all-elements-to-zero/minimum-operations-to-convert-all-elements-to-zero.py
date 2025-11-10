class Solution:
    def minOperations(self, a: List[int]) -> int:
        res,st = 0,[]
        for v in chain(a,[0]):
            while st and st[-1]>=v: res += st.pop()>v
            st.append(v)
        return res