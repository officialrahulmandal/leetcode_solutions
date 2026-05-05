class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inorder = [0] * numCourses

        for child, parent in prerequisites:
            adj[parent].append(child)
            inorder[child]+=1

        queue = collections.deque([i for i in range(numCourses) if inorder[i]==0])

        results=[]
        while queue:
            element = queue.popleft()
            results.append(element)
            for neighbour in adj[element]:
                inorder[neighbour] -= 1
                if inorder[neighbour]==0:
                    queue.append(neighbour)

        return True if len(results)==numCourses else False


        