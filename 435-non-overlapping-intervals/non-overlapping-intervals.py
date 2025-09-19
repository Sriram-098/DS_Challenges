class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        ls=[]
        end=intervals[0][1]
        count=0
        for i in range(1,len(intervals)):
            if end<=intervals[i][0]:
                end=intervals[i][1]
            else:
                count+=1
        return count
            
        