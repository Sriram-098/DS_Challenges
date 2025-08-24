from functools import lru_cache

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #@lru_cache(None)
        dp=[-1]*len(arr)
        def check(i):
            if i==len(arr):
                return 0
            if dp[i]!=-1:
                return dp[i]
            currmax=0
            maxi=0
            for j in range(i,min(i+k,len(arr))):
                currmax=max(currmax,arr[j])
                length=j-i+1
                maxi=max(maxi,(currmax*length)+check(j+1))
                dp[i]=maxi
            return dp[i]

        return check(0)
        
        
