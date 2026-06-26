class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        total = 0
        max_ = 0

        while left<right:
            cap = min(height[left],height[right])
            max_ = max(max_, cap*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right -= 1
            
        return max_
        