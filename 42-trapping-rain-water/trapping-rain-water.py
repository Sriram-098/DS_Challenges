class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0]*len(height)
        right=[0]*len(height)
        maxi=0
        for i in range(len(height)):
            maxi=max(height[i],maxi)
            left[i]=maxi
        maxi=0
        for i in range(len(height)-1,-1,-1):
            maxi=max(height[i],maxi)
            right[i]=maxi
        
        ans=0
        for i in range(len(height)):
            if height[i]<left[i] and height[i]<right[i]:
                mini=min(left[i],right[i])
                ans+=abs(height[i]-mini)
        return ans


        