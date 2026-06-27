class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjMatrix = [[] for _ in range(numCourses)]
        for child, parent in prerequisites:
            adjMatrix[parent].append(child)
            indegree[child]+=1

        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for i in adjMatrix[node]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)

        return numCourses == visited



            
        