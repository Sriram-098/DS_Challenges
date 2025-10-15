class Solution:
    def trap(self, height: List[int]) -> int:
        r=[0]*len(height)
        l=[0]*len(height)
        maxi=0
        for i in range(len(height)):
            maxi=max(height[i],maxi)
            l[i]=maxi
        maxi=0
        for i in range(len(height)-1,-1,-1):
            maxi=max(height[i],maxi)
            r[i]=maxi

        water=0
        mini=1e9
        for i in range(len(height)):
            if height[i]<l[i] and height[i]<r[i]:
                mini=min(l[i],r[i])
                water+=(mini-height[i])
        return water
        