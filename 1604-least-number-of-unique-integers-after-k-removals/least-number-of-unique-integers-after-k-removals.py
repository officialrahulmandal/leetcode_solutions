class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = defaultdict(int)
        for num in arr:
            freq[num] += 1

        min_heap = []
        for value in freq.values():
            heapq.heappush(min_heap, value)

        while k > 0:
            top = heapq.heappop(min_heap)
            if k >= top:
                k -= top
            else:
                heapq.heappush(min_heap, top - k)
                k = 0

        return len(min_heap)