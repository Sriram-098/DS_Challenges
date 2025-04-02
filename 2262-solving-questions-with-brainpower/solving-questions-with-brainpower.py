
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[-1]*len(questions)
        return self.f(0,questions,dp)

    def f(self,i,questions,dp):
        if(i==len(questions)-1):
            return questions[i][0]
        if (i>len(questions)-1):
            return 0
        if(dp[i]!=-1):
            return dp[i]
        nonpick=self.f(i+1,questions,dp)
        pick=questions[i][0]+self.f(i+questions[i][1]+1,questions,dp)
        dp[i]=max(pick,nonpick)
        return dp[i]
        