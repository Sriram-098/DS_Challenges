class Solution:
    def minDays(self, days: List[int], m: int, k: int) -> int:
        if m*k>len(days):
            return -1
        ans=max(days)

        low=min(days)
        high=max(days)
        while(low<=high):
            mid=(low+high)//2
            check=self.f(days,mid,k)   
            if check>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans     


    def f(self,days,x,k):
        count=0
        req=0
        for i in range(len(days)):
            if days[i]<=x:
                count+=1
            else:
                req+=int(count/k)
                count=0
        if days[len(days)-1]<=x:
            req+=int(count/k)
        
        return req
