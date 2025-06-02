class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        while(low<=high):
            mid=(low+high)//2
            num_hrs=self.f(piles,mid,h)
            if num_hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans



    def f(self,piles,x,h):
        ans=0
        for i in range(len(piles)):
            ans+=math.ceil(piles[i]/x)
            
        return ans


        