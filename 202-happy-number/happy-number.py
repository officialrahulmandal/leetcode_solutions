class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle=[]
        while(n is not 0):
            sum=0
            n=str(n)
            for i in n:
                sum+=int(i)*int(i)
            if sum==1:
                return True
            else:
                if sum in cycle:
                    return False
                cycle.append(sum)
                n=sum

        