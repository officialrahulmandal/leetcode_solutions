import operator
class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        store={}
        for element in arr:
            if element in store:
                store[element]+=1
            else:
                store[element]=1
        stored = list(store.values())
        stored.sort()
        i=0
        while(k>0):
            if k==0:
                break
            if k>=stored[i]:
                k-=stored[i]
                stored.pop(0)
                continue                    
            else:
                t=k
                k-=stored[i]
                stored[i]-=t
                if stored[i]==0:
                    stored.pop(0)
                    continue 
                
                break
                
                
        return len(stored)
        
