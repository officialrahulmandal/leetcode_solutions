class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        positive_index=0
        negative_index=1
        i=0
        len_arr=len(nums)-1
        result_array=[0]*(len_arr+1)
        #print(result_array)
        while(i<=len_arr):
            if nums[i]>=0:
                #print(positive_index,nums[i])
                result_array[positive_index] = nums[i]
                positive_index+=2
            elif nums[i]<0:
                result_array[negative_index] = nums[i]
                negative_index+=2
            i+=1
        return result_array

        