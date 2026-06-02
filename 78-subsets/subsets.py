class Solution:
    def helper(nums):
        num
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        curr = []
        def backtrack(i):
            if i==len(nums):
                subset.append(curr[:])
                return

            #include
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
            #exclude
            backtrack(i+1)

        backtrack(0)
        return subset


        
        