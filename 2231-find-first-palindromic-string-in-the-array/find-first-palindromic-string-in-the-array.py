class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            i=0
            j=len(word)-1
            while(i<j):
                if word[i]==word[j]:
                    i+=1
                    j-=1
                else:
                    break
            half=len(word)//2
            if i>=half and j<=half:
                return word
            else:
                continue
        return ''
        