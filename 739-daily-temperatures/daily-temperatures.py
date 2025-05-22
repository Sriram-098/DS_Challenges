class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        st=[]
        for i in range(len(temperatures)-1,-1,-1):
            while st and temperatures[i]>=st[-1][0]:
                st.pop()

            if st:
                ans[i]=st[-1][1]-i
            
            st.append((temperatures[i],i))

        return ans

            
            
            
        