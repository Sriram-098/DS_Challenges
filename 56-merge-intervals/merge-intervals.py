class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            if len(ans)==0 or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])

            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        return ans

        