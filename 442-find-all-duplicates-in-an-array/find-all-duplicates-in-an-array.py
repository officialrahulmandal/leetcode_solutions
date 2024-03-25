class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        store=set()
        dups = []
        for num in nums:
            if num in store:
                dups.append(num)
            else:
                store.add(num)
        return dups

        