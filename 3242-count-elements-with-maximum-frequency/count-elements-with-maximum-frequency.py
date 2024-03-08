class Solution:
    def maxFrequencyElements(self, nums):
        mp = {}
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        count = 0
        max_freq = float('-inf')
        for freq in mp.values():
            max_freq = max(max_freq, freq)

        for freq in mp.values():
            if freq == max_freq:
                count += max_freq

        return count