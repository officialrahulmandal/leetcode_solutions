class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        j=i+1
        best=0
        len_arr = len(prices)
        while (j<len(prices)):
            if (prices[j]-prices[i]<0):
                i=j
                j+=1
            else:
                best=max(best, prices[j]-prices[i])
                j+=1
        return best
        