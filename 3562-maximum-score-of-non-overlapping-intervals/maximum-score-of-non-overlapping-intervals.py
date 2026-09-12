import functools
from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # 1. Store intervals with their original index: [start, end, weight, orig_idx]
        sorted_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            sorted_intervals.append((l, r, w, i))
            
        # 2. Sort primarily by start time.
        sorted_intervals.sort(key=lambda x: x[0])
        n = len(sorted_intervals)
        
        # Extract only start times to use for binary searching the next valid interval
        starts = [x[0] for x in sorted_intervals]
        
        # 3. DP with Memoization
        # dp(i, count) returns a tuple: (max_weight, tuple_of_selected_indices)
        @functools.lru_cache(None)
        def solve(i: int, count: int):
            if count == 4 or i == n:
                return (0, ())
            
            # Option 1: Skip the current interval
            res_weight, res_indices = solve(i + 1, count)
            
            # Option 2: Take the current interval
            start, end, weight, orig_idx = sorted_intervals[i]
            
            # Find the next interval that starts strictly after the current one ends
            # Using bisect_right to find the first interval with start_time > current_end
            next_idx = bisect_right(starts, end)
            
            next_weight, next_indices = solve(next_idx, count + 1)
            take_weight = weight + next_weight
            take_indices = (orig_idx,) + next_indices
            
            # 4. Compare options based on maximum weight and lexicographical order
            if take_weight > res_weight:
                res_weight, res_indices = take_weight, take_indices
            elif take_weight == res_weight:
                # If weights are tied, select the combination with the lexicographically smaller sorted indices
                if sorted(take_indices) < sorted(res_indices):
                    res_indices = take_indices
                    
            return res_weight, res_indices

        # Get the result from the DP function
        _, optimal_indices = solve(0, 0)
        
        # Return the indices sorted as requested by the problem statement
        return sorted(optimal_indices)
