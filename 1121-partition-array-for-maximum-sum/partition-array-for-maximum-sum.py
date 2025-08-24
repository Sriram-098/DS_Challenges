from functools import lru_cache

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def check(i):
            if i==len(arr):
                return 0
            currmax=0
            maxi=0
            for j in range(i,min(i+k,len(arr))):
                currmax=max(currmax,arr[j])
                length=j-i+1
                maxi=max(maxi,(currmax*length)+check(j+1))
            return maxi

        return check(0)
        
        
