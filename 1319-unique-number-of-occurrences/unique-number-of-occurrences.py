class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for a in arr:
            if a in freq:
                freq[a]+=1
            else:
                freq[a]=1
        value = list(freq.values())
        return len(value)==len(set(value))
        