class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        placeholder = set()
        l_ss=0
        l=0
        for r in range(len(s)):
            while s[r] in placeholder:
                placeholder.remove(s[l])
                l+=1
            placeholder.add(s[r])
            l_ss=max(l_ss, r-l+1)
        return l_ss
                