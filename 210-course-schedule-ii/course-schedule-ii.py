class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder=[[] for _ in range(numCourses) ]
        order = [0] * numCourses
        for child,parent in prerequisites:
            inorder[parent].append(child)
            order[child]+=1
        
        queue = collections.deque([i for i in range(numCourses) if order[i]==0 ])
        print(queue)

        result = []
        while queue:
            element= queue.popleft()
            result.append(element)

            for neighbour in inorder[element]:
                order[neighbour]-=1
                if order[neighbour]==0:
                    print(neighbour)
                    queue.append(neighbour)

        return result if len(result)==numCourses else []



        