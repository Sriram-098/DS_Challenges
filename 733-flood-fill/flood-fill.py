from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        change=image[sr][sc]
        image[sr][sc]=color
        q=deque()
        q.append((sr,sc))
        dirs=((-1,0),(0,1),(1,0),(0,-1))
        vis=[[0]*len(image[0]) for _ in range(len(image))]
        while q:
            r,c=q.popleft()
            for i,j in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(image) and 0<=nc<len(image[0]) and image[nr][nc]==change and vis[nr][nc]==0:
                    image[nr][nc]=color
                    vis[nr][nc]=1
                    q.append((nr,nc))
        return image


        

    

        