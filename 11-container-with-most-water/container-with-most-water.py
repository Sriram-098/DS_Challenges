class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        l=0
        r=len(height)-1
        ans=0
        while(l<r):
            m=min(height[l],height[r])
            ans=max(ans,m*(r-l))
            
            
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return ans

            
        