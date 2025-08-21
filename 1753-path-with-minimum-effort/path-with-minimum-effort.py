from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs=((-1,0),(1,0),(0,1),(0,-1))
        pq=PriorityQueue()
        pq.put((0,0,0))
        dis=[[1e9]*len(heights[0]) for _ in range(len(heights))]
        dis[0][0]=0
        while not pq.empty():
            diff,i,j=pq.get()
            print(diff,i,j)
            if i==len(heights)-1 and j==len(heights[0])-1:
                return diff
            for r,c in dirs:
                nr=i+r
                nc=j+c
                if 0<=nr<len(heights) and 0<=nc<len(heights[0]) and max(diff,abs(heights[i][j]-heights[nr][nc]))<dis[nr][nc]:
                    dis[nr][nc]=max(diff,abs(heights[i][j]-heights[nr][nc]))
                    pq.put((max(diff,abs(heights[i][j]-heights[nr][nc])),nr,nc))
        return 0




        