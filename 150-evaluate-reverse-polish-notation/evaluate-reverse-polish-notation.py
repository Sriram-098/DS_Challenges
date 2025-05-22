class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if len(st)>1 and (i=="+"  or i=="-" or i=="*" or i=="/"):
                s2=int(st.pop())
                s1=int(st.pop())
                ans=0
                if i=="+":
                    ans=s1+s2
                if i=="-":
                    ans=s1-s2
                if i=="*":
                    ans=s1*s2
                if i=="/":
                    ans=s1/s2
                
                st.append(int(ans))
            elif -201 <int(i)<201:
                st.append(i)

           
        return int(st[0])

            



















        