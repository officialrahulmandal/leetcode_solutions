from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = []
        for num, freq in sorted_items:
            res.append(num)
            if len(res) == k:
                return res
    