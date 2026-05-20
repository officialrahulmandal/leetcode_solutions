from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, f in freq.items():
            buckets[f].append(x)
        out = []

        for f in range(len(buckets) - 1, 0, -1):
            out.extend(buckets[f])
            if len(out) >= k:
                return out[:k]
        return out
        