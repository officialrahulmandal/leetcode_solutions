class Solution:
    def distributeCandies(self, n: int, m: int) -> int:
        res=(n+2)*(n+1)//2
        for i in range(1,4):
            if n-i*(m+1)<0:
                break
            res+=(-1)**i*comb(3,i)*(n-i*(m+1)+2)*(n-i*(m+1)+1)//2
        return res