class Solution:
    def candy(self, ratings: List[int]) -> int:
        dappi=[1 for j in range(len(ratings))]
        k=len(ratings)
        j=0
        for j in range(1,len(ratings)):
            if ratings[j]>ratings[j-1]:
                dappi[j]=dappi[j-1]+1
        rat=ratings[::-1]
        dappi=dappi[::-1]
        for j in range(1,len(rat)):
            if rat[j]>rat[j-1]:
                if dappi[j]<dappi[j-1]+1:

                    dappi[j]=dappi[j-1]+1
        print(dappi)
        return sum(dappi)
        
        