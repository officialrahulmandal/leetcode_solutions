class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        store = set()
        start = 0
        store.add(s[start])
        max_ = 1

        for i in range(1, len(s)):
            if s[i] in store:
                while s[i] in store:
                    store.remove(s[start])
                    start+=1
            
            store.add(s[i])

            max_ = max(max_, i-start+1)
            
        return max_
                    

        