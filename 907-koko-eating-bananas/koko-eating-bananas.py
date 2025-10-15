class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def f(x,piles):
            count=0
            for i in range(len(piles)):
                if piles[i]<=x:
                    count+=1
                else:
                    count+=math.ceil(piles[i]/x)
            return count
        l=1
        r=max(piles)
        ans=0
        while l<=r:
            mid=(l+r)//2
            check=f(mid,piles)
            
            if check<=h:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        