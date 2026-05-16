import queue

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # building adj list

        n = len(isConnected)
        count = 0
        adj = [[] for _ in range(n+1) ]
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if isConnected[i][j] == 1:
                    adj[i+1].append(j+1)
        
        visited = set()

        def bfs(node):
            q = queue.deque()
            q.append(node)
            visited.add(node)

            while q:
                curr = q.popleft()
                for i in adj[curr]:
                    if i not in visited:
                        q.append(i)
                        visited.add(i)


        for i in range(1, n+1):
            if i not in visited:
                bfs(i)
                count +=1

        return count
                

            

            
        