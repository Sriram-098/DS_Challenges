class Solution:
    def calculate(self, s: str) -> int:
        num=0
        st=[]
        s=s.replace(" ","")
        sign="+"
        print(s)
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10 +int(s[i])

            if s[i] in "+-*/" or i==len(s)-1:
                if sign=="+":
                    st.append(num)
                if sign=="-":
                    st.append(-num)
                if sign=="*":
                    st.append(st.pop()*num)
                if sign=="/":
                    prev=st.pop()
                    st.append(int(prev/num))

                num=0
                sign=s[i]

        return sum(st)

        

        
        
        