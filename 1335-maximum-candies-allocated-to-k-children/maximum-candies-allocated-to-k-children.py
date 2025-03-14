class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if(sum(candies)<k):
            return 0
        s=1
        ans=0
        e=max(candies)
        while(s<=e):
            m=(s+e)//2
            child=sum(c//m for c in candies)
            if(child>=k):
                ans=m
                s=m+1
            else:
                e=m-1
        return ans

       
        