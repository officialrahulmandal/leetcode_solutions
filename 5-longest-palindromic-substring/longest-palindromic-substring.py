class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        maxLength = 0

        for i in range(len(s)):
            #for odd centre
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>maxLength:
                    result=s[left:right+1]
                    maxLength=right-left+1
                left-=1
                right+=1
                
                
                
            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if (right-left+1)>maxLength:
                    result=s[left:right+1]
                    maxLength=right-left+1
                left-=1
                right+=1
                
        return result