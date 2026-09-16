class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0]*len(temperatures)
        st=[]
        for i in range(len(temperatures)-1,-1,-1):
            
            while st and st[-1][0]<=temperatures[i]:
                st.pop()
            if st:
                ans[i]=st[-1][1]-i
            st.append([temperatures[i],i])
        return ans

        