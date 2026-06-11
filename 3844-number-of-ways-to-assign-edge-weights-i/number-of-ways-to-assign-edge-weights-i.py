class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def binary_exp(a, b):
            MOD = 10**9 + 7
            if b==0:
                return 1
            half_power = binary_exp(a, b//2)
            power = (half_power * half_power) % MOD

            if b % 2:
                return (power * a) % MOD

            return power

        def find_depth(adj, adj_list, parent):
            max_depth = -1
            for c in adj_list.get(adj,[]):
                if c == parent:
                    continue
                depth = find_depth(c, adj_list, adj)
                max_depth = max(max_depth, depth)
            return max_depth + 1

        adj_list  = {}

        for p, c in edges:
            adj_list.setdefault(p, []).append(c)
            adj_list.setdefault(c, []).append(p)
        depth = find_depth(1, adj_list, -1)
        return binary_exp(2, depth-1)

        


        

            
        