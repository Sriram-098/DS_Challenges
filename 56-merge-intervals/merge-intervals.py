class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]

            if(len(ans)>0 and ans[-1][1]>=intervals[i][0]):
                continue

            for j in range(i+1,len(intervals)):
                if end>=intervals[j][0]:
                    end=max(end,intervals[j][1])
                else:
                    break

            l=[start,end]
            ans.append(l)
        return ans