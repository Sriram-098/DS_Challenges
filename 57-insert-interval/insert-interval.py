class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ls=[]
        for i in range(len(intervals)):
            if len(ls)==0 or ls[-1][1]<intervals[i][0]:
                ls.append(intervals[i])
            else:
                ls[-1][1]=max(ls[-1][1],intervals[i][1])
        return ls
        