class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st=[]
        for i in range(len(num)):
            
            while st and k>0 and int(st[-1])>int(num[i]):
                st.pop()
                k-=1
            st.append(num[i])
       
        while st and k>0 :
            st.pop()
            k-=1
        
        while st and st[0]=="0":
            st.pop(0)

        return ("".join(st)) if st else "0"

        