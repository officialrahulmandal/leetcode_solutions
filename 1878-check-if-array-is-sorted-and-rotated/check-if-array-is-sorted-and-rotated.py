class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums)==0 or len(nums)==1:
            return True
        find_max=0
        min_bef=9999
        flip=False
        last=None
        for i in nums:
            if last is None:
                if find_max<i:
                    find_max=i
                if min_bef>i:
                    min_bef=i
                last=i
                continue
            elif flip and i>find_max:
                return False
            elif flip and i<find_max:
                if min_bef<i:
                    return False
                if i<last:
                    return False
                else:
                    last=i
            else:
                if i<last:
                    if min_bef<i:
                        return False
                    if find_max<i:
                        find_max=i
                    flip=True
                    last=i
                else:
                    if find_max<i:
                        find_max=i
                    if min_bef>i:
                        min_bef=i
                    last=i
                    continue
        return True


        