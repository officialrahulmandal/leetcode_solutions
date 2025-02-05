class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        find_diff=[]
        diff_calc=0
        i=0
        j=0
        while i<len(s1) and j<len(s2):
            if s1[i]!=s2[j]:
                find_diff.append(i)
                find_diff.append(j)
                i+=1
                j+=1
                diff_calc+=1
            else:
                i+=1
                j+=1
        if diff_calc>2 or diff_calc==1:
            return False
        elif diff_calc==0:
            return True
        elif diff_calc==2:
            if s1[find_diff[0]]==s2[find_diff[3]] and s1[find_diff[2]]==s2[find_diff[1]]:
                return True
            else:
                return False
            
            



        