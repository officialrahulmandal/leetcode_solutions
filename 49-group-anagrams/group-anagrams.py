class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results=dict()
        for w in strs:
            word = ''.join(sorted(w))
            if word in results:
                results[word].append(w)
            else:
                results[word]=[w]

        return list(results.values())
        