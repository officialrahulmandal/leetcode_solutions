class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        counter=1
        temp=a
        while(len(a)<len(b)):
            a+=temp
            counter+=1
            
        if b in a:
            return counter
            
        if b in a+temp:
            return counter+1
            
        return -1
        