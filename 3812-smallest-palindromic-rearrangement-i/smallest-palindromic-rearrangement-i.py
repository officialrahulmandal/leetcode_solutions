class Solution:
    def smallestPalindrome(self, s: str) -> str:
        alphabets = [0] * 26

        for a in s:
            alphabets[ord(a)-ord('a')] += 1
            
        result = [''] * len(s)
        left=0
        right=len(result)-1

        for a in range(len(alphabets)):
            while alphabets[a]>=2:
                result[left]=chr(ord('a')+a)
                result[right]=chr(ord('a')+a)
                left+=1
                right-=1
                alphabets[a]-=2
            while alphabets[a]==1:
                result[len(result)//2]=chr(ord('a')+a)
                alphabets[a]-=1

        return ''.join(result)


        