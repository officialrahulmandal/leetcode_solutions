class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1)>len(arr2):
            arr1, arr2 = arr2, arr1

        store = set()
        result = 0

        for v1 in arr1:
            while v1 and v1 not in store:
                store.add(v1)
                v1=v1//10
                

        for n in arr2:
            while n and n not in store:
                n = n//10

            if n:
                result = max(result, len(str(n)))

        return result


        