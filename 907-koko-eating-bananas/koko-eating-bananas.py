class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        def min_per_hr(x):
            count=0
            for i in range(len(piles)):
                count+=math.ceil(piles[i]/x)
            return count
        while low<=high:
            mid=(low+high)//2
            k=min_per_hr(mid)
            print(k)
            if k<=h:
                print(mid)
                high=mid-1
                ans=mid
            else:
                low=mid+1
                

        return ans
        