import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        m = len(nums)
        n = m // 3
        left = [0] * m
        maxheap = []
        prefSum = 0
        for i in range(n):
            prefSum += nums[i]
            heapq.heappush(maxheap, -nums[i])
        left[n-1] = prefSum
        for i in range(n, m):
            heapq.heappush(maxheap, -nums[i])
            val = -heapq.heappop(maxheap)
            prefSum += nums[i] - val
            left[i] = prefSum

        right = [0] * m
        minheap = []
        suffSum = 0
        for i in range(m-1, m-n-1, -1):
            suffSum += nums[i]
            heapq.heappush(minheap, nums[i])
        right[m-n] = suffSum
        for i in range(m-n-1, -1, -1):
            heapq.heappush(minheap, nums[i])
            val = heapq.heappop(minheap)
            suffSum += nums[i] - val
            right[i] = suffSum

        diff = float('inf')
        for i in range(n-1, 2*n):
            diff = min(diff, left[i] - right[i+1])
        return diff