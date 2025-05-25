class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st=[]
        a=len(heights)
        ans=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            count=0
            while st and st[-1]<heights[i]:
                st.pop()
                count+=1
            if st :
                count+=1
            ans[i]=count

            st.append(heights[i])

        return ans
       

     

