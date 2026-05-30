class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]: return image
        row = len(image)
        column = len(image[0])
        if color == image[sr][sc]:
            return image

        def dfs(sr, sc, color, oc):
            direction = [[0,-1],[0,1],[1,0],[-1,0]]

            if sr>=0 and sr<=row-1 and sc>=0 and sc<=column-1:
                if image[sr][sc] == oc:
                    image[sr][sc]=color
                    for r, c in direction:
                        dfs(sr+r,sc+c, color, oc) 


        dfs(sr, sc, color, image[sr][sc])

        return image
        