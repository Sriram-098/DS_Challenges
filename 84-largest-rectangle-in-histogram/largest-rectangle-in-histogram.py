class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        r=[len(heights)]*len(heights)
        l=[-1]*len(heights)
        st=[]
        for i in range(len(heights)):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                l[i]=st[-1]
            st.append(i)
        
        #print(l)
        st=[]
        for i in range(len(heights)-1,-1,-1):
            while st and heights[st[-1]]>=heights[i]:
                st.pop()
            if st:
                r[i]=st[-1]
            st.append(i)
        print(l,r)
        maxi=0
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(r[i]-l[i]-1))
        return maxi
            

        