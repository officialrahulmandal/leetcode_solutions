class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        placeholder=set()
        j=0
        len_arr=range(len(s))
        max_ss=0
        for i in range(len(s)):
            while s[i] in placeholder:
                placeholder.remove(s[j])
                j+=1
            placeholder.add(s[i])
            max_ss=max(max_ss,len(placeholder))
        return max_ss