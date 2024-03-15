import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = []

        for stone in stones:
            heapq.heappush(data, -1*stone)
        
        while len(data)>1:
            last_element = -1 * heapq.heappop(data)
            second_last = -1 * heapq.heappop(data)
             
            if second_last == last_element:
                continue
            elif second_last < last_element:
                heapq.heappush(data, -1*(last_element-second_last))

        if len(data) == 0:
            return 0
        else:
            return -1 * data[0]
                


        