class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x:x[1])
        ls=[]
        print(intervals)
        for i in range(len(intervals)):
            if len(ls)==0:
                ls.append(intervals[i])
            elif ls[-1][1]<=intervals[i][0]:
                ls.append(intervals[i])
        return abs(len(intervals)-len(ls))
        