class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[]
        for i in range(len(intervals)):
            if len(ans)==0 or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans
        
        