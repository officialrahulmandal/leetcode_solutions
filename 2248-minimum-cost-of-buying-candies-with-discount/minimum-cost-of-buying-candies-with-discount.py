class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        current=None
        prev=None
        total_cost=0
        i=len(cost)-1
        while i>=0:
            if current is None:
                total_cost+=cost[i]
                current=cost[i]
                i-=1
                continue
            if prev is None:
                total_cost+=cost[i]
                prev=cost[i]
                i-=1
                continue
            if current and prev:
                current=None
                prev=None
                i-=1
                continue

        return total_cost


        