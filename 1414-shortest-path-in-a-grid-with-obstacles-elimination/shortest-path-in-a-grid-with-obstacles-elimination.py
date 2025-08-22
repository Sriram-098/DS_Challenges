from collections import deque
from queue import PriorityQueue
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        pq=PriorityQueue()
        pq.put((0,0,0,0))
        dirs=((0,-1),(1,0),(-1,0),(0,1))
        vis=set()
        vis.add((0,0,0))
        while not pq.empty():
            #print(pq.queue)
            steps,m,i,j=pq.get()
            
            if i==len(grid)-1 and j==len(grid[0])-1:
                return steps
           
            for r,c in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                    obstacle=m+grid[nr][nc]
                    if  m<=k and (nr,nc,obstacle) not in vis:
                        pq.put((steps+1,obstacle,nr,nc))
                        vis.add((nr,nc,obstacle))

        return -1
                    
        

        