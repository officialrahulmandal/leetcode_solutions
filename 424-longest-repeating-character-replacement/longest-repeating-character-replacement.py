class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        store = {}
        longest = 0
        max_freq = 0

        for i in range(len(s)):
            store[s[i]] = store.get(s[i], 0) + 1

            max_freq = max(max_freq, store[s[i]])

            

            while (i-start+1)-max_freq > k:
                store[s[start]] -= 1
                start += 1

            longest = max(longest, i-start+1)

        return longest
                 
        