import queue
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # first using bfs
        v = len(isConnected)
        count = 0
        adj = [[] for _ in range(v)]
        visited = [False] * v
        for i in range(v):
            for j in range(v):
                if i==j:
                    continue
                if isConnected[i][j]==1:
                    adj[i].append(j)
                    #visited[i] =  True
            
        
        for i in range(v):
            if not visited[i]:
                q = queue.deque()
                q.append(i)
                visited[i] = True
                count+=1
                
                while q:
                    curr = q.popleft()
                    visited[curr] = True
                    for value in adj[curr]:
                        if not visited[value]:
                            q.append(value)
                    
        
        return count

        
        
        