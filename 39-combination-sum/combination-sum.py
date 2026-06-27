class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def dfs(i ,curr , total):
            if total == target:
                results.append(curr.copy())
                return

            if total > target or i>=len(candidates):
                return

            # included
            curr.append(candidates[i])
            dfs(i, curr, total+candidates[i] )

            curr.pop()
            dfs(i+1, curr, total )




            # not included




        dfs(0 ,[] , 0)
        return results
        