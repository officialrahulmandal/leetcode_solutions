import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = []

        for num in nums:
            heapq.heappush(data, num)
            if len(data)>k:
                heapq.heappop(data)

        return data[0]

        