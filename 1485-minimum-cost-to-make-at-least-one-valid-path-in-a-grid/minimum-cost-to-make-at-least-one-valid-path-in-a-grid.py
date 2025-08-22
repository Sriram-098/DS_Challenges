from queue import PriorityQueue
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        pq=PriorityQueue()
        pq.put((0,0,0))
        dirs=((-1,0),(1,0),(0,1),(0,-1))
        vis=[[0]*len(grid[0]) for _ in range(len(grid))]
        
        while not pq.empty():
          
            count,i,j=pq.get()
            
            
            if vis[i][j]==1:
                continue
            vis[i][j]=1
            if i==len(grid)-1 and j==len(grid[0])-1:
                return count
            
          
            
            for r,c in dirs:
                nr=i+r
                nc=j+c
                
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]==0 and grid[i][j]==1 and nr==i and nc==j+1:
                    pq.put((count,nr,nc))
                    
                    
                elif 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]==0 and grid[i][j]==2 and nr==i and nc==j-1:
                    pq.put((count,nr,nc))
                 
                    
                elif 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]==0 and grid[i][j]==3 and nr==i+1 and nc==j:
                    pq.put((count,nr,nc))
                 
               
                elif 0<=nr<len(grid) and 0<=nc<len(grid[0]) and vis[nr][nc]==0 and grid[i][j]==4 and nr==i-1 and nc==j:
                    pq.put((count,nr,nc))
                  
                    
                elif 0<=nr<len(grid) and 0<=nc<len(grid[0])  and vis[nr][nc]==0:
                     
                    pq.put((count+1,nr,nc))
                   
        return -1





            








      

        