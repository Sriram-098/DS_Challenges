class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis=[[-1]*len(grid[0]) for _ in range(len(grid))]

        def check(i,j):
            dirs=((-1,0),(1,0),(0,1),(0,-1))
            ans=0
            for a,b in dirs:
                nr=a+i
                nc=b+j
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                    ans+=1
            return ans
        count_1=0
        sub=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count_1+=1
                    sub+=check(i,j)

        total=count_1*4
        ans=total-sub
        return ans
        

        
        