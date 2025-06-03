class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        ans=0
        def f(weights,mid,days):
            
            seperate_weights=0
            seperate_days=0
            for i in range(len(weights)):
                if seperate_weights+weights[i]>mid:
                    seperate_days+=1
                    seperate_weights=0
                seperate_weights+=weights[i]
            seperate_days+=1
        
        
            return seperate_days<=days
    
        while(low<=high):
            mid=(low+high)//2
            check=f(weights,mid,days)
            if check:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

        