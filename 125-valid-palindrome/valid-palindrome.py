class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start<end:
            while not self.isAlphaNum(s[start]) and start<end:
                start+=1

            while not self.isAlphaNum(s[end]) and start<end:
                end-=1

            if s[start].lower()!=s[end].lower():
                return False

            start+=1
            end-=1

        return True
            


    def isAlphaNum(self, c):
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')  
        