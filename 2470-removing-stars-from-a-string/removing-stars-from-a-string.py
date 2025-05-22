class Solution:
    def removeStars(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            ch=s[i]
            if len(st)>0 and ch=='*':
                st.pop()
            
            else:
                st.append(ch)

        return "".join(st)
        