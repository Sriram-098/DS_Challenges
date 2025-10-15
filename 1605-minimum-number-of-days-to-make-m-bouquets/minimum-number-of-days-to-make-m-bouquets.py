class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        def f(x,k):
            count=0
            ans=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=x:
                    count+=1
                else:
                    ans+=(count//k)
                    count=0
            ans+=(count//k)
            return ans

        l=min(bloomDay)
        r=sum(bloomDay)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            check=f(mid,k)
            print(mid,check)
            if check>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans

        