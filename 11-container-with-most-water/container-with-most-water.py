class Solution:
    def maxArea(self, height: List[int]) -> int:
        storage = 0
        i = 0
        j = len(height)-1

        while i<j:
            containes = min(height[i], height[j]) * (j-i)

            if containes > storage:
                storage = containes
            
            if height[i] > height[j]:
                j-=1

            else:
                i+=1

        return storage

        