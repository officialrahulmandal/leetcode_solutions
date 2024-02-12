def partSort(arr, N, a, b):
     
    # Variables to store start and
    # end of the index range 
    l = min(a, b)
    r = max(a, b)
 
    # Temporary array 
    temp = [0 for i in range(r - l + 1)]
    j = 0
    for i in range(l, r + 1, 1):
        temp[j] = arr[i]
        j += 1
     
    # Sort the temporary array 
    temp.sort(reverse = False)
 
    # Modifying original array with
    # temporary array elements 
    j = 0
    for i in range(l, r + 1, 1):
            arr[i] = temp[j]
            j += 1
 
    # Print the modified array 
    return arr

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_arr=len(nums)
        peak_index=-1
        new_index=-1
        for i in range(1,len_arr):
            if nums[i]>nums[i-1]:
                peak_index=i
        if peak_index==-1:
            for i in range(len_arr//2):
                nums[i],nums[len_arr-i-1]=nums[len_arr-i-1],nums[i]
        else:
            for i in range(peak_index+1,len_arr):
                if nums[i]<nums[peak_index] and nums[i]> nums[peak_index-1]:
                    new_index=i
            if new_index==-1:
                nums[peak_index],nums[peak_index-1]=nums[peak_index-1],nums[peak_index]
            else:
                nums[new_index],nums[peak_index-1]=nums[peak_index-1],nums[new_index]
            nums=partSort(nums,len(nums[peak_index:len_arr-1]),peak_index,len_arr-1)
        return nums

                    


        