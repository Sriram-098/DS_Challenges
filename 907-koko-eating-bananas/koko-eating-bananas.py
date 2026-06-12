class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(mid):
            count=0
            for i in range(len(piles)):
                count+=(ceil(piles[i]/mid))
            return count

        l=1
        r=max(piles)
        while l<=r:
            mid=(l+r)//2
            check=f(mid)

            if check <=h:
                ans=mid
                r=mid-1

            else:
                l=mid+1

        return ans


        