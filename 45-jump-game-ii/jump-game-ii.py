class Solution(object):
    def jump(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump=0
        l=r=0
        while(r<len(array)-1):
            reach = 0
            for z in range(l, r+1):
                reach=max(reach, z+ array[z])
            l=r+1
            r=reach
            jump+=1
        return jump
        