class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque()
        original_color=image[sr][sc]
        image[sr][sc]=color
        q.append((sr,sc))
        vis=[[0]*len(image[0]) for _ in range(len(image))]
        vis[sr][sc]=1
        dirs=((0,1),(1,0),(-1,0),(0,-1))
        while q:
            r,c=q.pop()
            for i,j in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(image) and 0<=nc<len(image[0]) and vis[nr][nc]==0 and image[nr][nc]==original_color:
                    image[nr][nc]=color
                    vis[nr][nc]=1
                    q.append((nr,nc))

        return image