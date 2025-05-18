class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi=0
        best=values[0]+0
        for j in range(1,len(values)):
            score=best+values[j]-j
            maxi=max(score,maxi)
            best=max(values[j]+j,best)
        return maxi

        