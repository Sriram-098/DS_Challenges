class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count=0
        
        points.sort()
        end=points[0][1]
        print(points)
        for i in range(1,len(points)):
            if(points[i][0]<=end):
                end=min(end,points[i][1])
                continue
            count+=1
            end=points[i][1]
        return count+1
        