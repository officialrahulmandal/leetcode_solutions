class Solution:
    def searchHelper(self, nums, target,left, right):
        if left>right:
            return -1
        mid = left+(right-left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.searchHelper(nums, target, left,mid-1)
        elif nums[mid]<target:
            return self.searchHelper(nums, target, mid+1,right)
        
    def search(self, nums: List[int], target: int) -> int:
        mid = (len(nums)//2)-1
        length = len(nums)
        value=mid
        return self.searchHelper(nums, target, 0, len(nums)-1)

        