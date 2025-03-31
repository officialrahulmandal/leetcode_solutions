class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        adj = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(adj[-k + 1 :]) - sum(adj[: k - 1]) if k != 1 else 0