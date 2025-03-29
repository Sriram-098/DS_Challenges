class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        for i in range(len(intervals)):
            
            if (len(ans)==0 or ans[-1][1]<intervals[i][0]):
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(intervals[i][1],ans[-1][1])
        return ans
                

        return ans