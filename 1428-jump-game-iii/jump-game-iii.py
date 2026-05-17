class Solution:
    def canReachHelperFunction(self, arr, visited, start):
        if visited[start]:
            return False
        out1=False
        out2=False
        value = arr[start]

        if value ==0:
            return True
        else: 
            visited[start] = True
            if 0 <= start + value < len(arr) and not visited[start + value]:
                out1 = self.canReachHelperFunction(arr, visited, start + value)
            if 0 <= start - value < len(arr) and not visited[start - value]:
                out2 = self.canReachHelperFunction(arr, visited, start - value)

        return out1 or out2


    def canReach(self, arr: List[int], start: int) -> bool:
        out1=False
        out2=False
        value = arr[start]
        visited = [False] * len(arr)
        visited[start] = True
        if value == 0:
            return True
        if value != 0:
            if 0 <= start + value < len(arr) and not visited[start + value]:
                out1 = self.canReachHelperFunction(arr, visited, start + value)
            if 0 <= start - value < len(arr) and not visited[start - value]:
                out2 = self.canReachHelperFunction(arr, visited, start - value)

        return out1 or out2
            


        