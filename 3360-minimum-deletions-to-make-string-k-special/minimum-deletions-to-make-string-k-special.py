class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        res = len(word)
        d = Counter(word)
        for c in d:
            res = min(res, sum(v if v < d[c] else max(0, v - d[c] - k) for v in d.values()))
        return res