class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for word in strs:
            w=''.join(sorted(word))
            store[w].append(word)
        return list(store.values())
        