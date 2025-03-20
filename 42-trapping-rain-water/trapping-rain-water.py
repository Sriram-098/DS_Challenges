class Solution:
    def trap(self, height: List[int]) -> int:

        lis1=self.uptoleft(height)
        lis2=self.uptoright(height)
        

        ans=0
        for i in range(len(height)):
            if height[i]<lis1[i] and height[i]<lis2[i]:
                m=min(lis1[i],lis2[i])
                ans+=(m-height[i])
        return ans



    def uptoleft(self,height):
        st=[]
        lis=[0]*len(height)
        m=0

        for i in range(len(height)):
            m=max(height[i],m)
            lis[i]=m 

        return lis

    def uptoright(self,height):
        st=[]
        lis=[0]*len(height)
        m=0

        for i in range(len(height)-1,-1,-1):
            m=max(height[i],m)
            lis[i]=m
            
           
        return lis





    



    
        