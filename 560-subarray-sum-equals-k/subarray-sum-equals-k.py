class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : 1}
        current_sum = 0
        count = 0

        for n in nums:
            current_sum += n
            if current_sum-k in prefix_sum:
                count += prefix_sum[current_sum-k]

            prefix_sum[current_sum] = prefix_sum.get(current_sum,0)+1


        return count


        