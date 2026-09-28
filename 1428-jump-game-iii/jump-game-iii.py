class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        dp=[False]*len(arr)
        dp[start]=False
        if arr[start]==0:
            return True
        def check(i):
            if i<0 or i>=len(arr) or dp[i]:
                return False
            if arr[i]==0 :
                return True
            dp[i]=True
            one_way=check(i-arr[i])
            ano_way=check(i+arr[i])
            dp[i]=one_way or ano_way
            return dp[i]
            
        return check(start)
        