class Solution:
    def minElement(self, nums: List[int]) -> int:

        add_digits = lambda num: sum(int(x) for x in str(num))

        return min(map(add_digits, nums))