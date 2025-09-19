class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for i in range(len(s)):
            ch=s[i]
            if st and st[-1]=='(' and ch==')':
                st.pop()
            else:
                st.append(ch)
        return len(st)
        