class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs=((0,-1),(-1,0),(1,0),(0,1))
        pacific=[[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic=[[False]*len(heights[0]) for _ in range(len(heights))]
        def dfs(i,j,vis):
            vis[i][j]=True
            for r,c in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and not vis[nr][nc] and heights[nr][nc]>=heights[i][j]:
                    dfs(nr,nc,vis)


        for i in range(len(heights)):
            dfs(i,0,pacific)
            dfs(i,len(heights[0])-1,atlantic)
        for i in range(len(heights[0])):
            dfs(0,i,pacific)
            dfs(len(heights)-1,i,atlantic)

        ans=[]
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans
        