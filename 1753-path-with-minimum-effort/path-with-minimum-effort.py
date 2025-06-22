from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq=PriorityQueue()
        effort=0
        r=0
        c=0
        pq.put((effort,r,c))
        
        
        vis=[[1e9]*len(heights[0]) for _ in range(len(heights))]
        vis[0][0]=0
        dirs=((-1,0),(1,0),(0,1),(0,-1))
        while not pq.empty():
            
            effort,r,c=pq.get()
            
            if r==len(heights)-1 and c==len(heights[0])-1:
                return effort
            for i,j in dirs:
                nr=r+i
                nc=c+j
                
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and  max(effort,abs(heights[nr][nc]-heights[r][c]))<vis[nr][nc]:
                    vis[nr][nc]=max(effort,abs(heights[nr][nc]-heights[r][c]))
                    
                    
                    pq.put((max(effort,abs(heights[nr][nc]-heights[r][c])),nr,nc))

        return 0

            


        