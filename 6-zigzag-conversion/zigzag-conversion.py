class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        d=0
        i=0
        x=0
        ans=[[] for _ in range(numRows)]
        print(ans)
        while(i<len(s)):
            ans[d].append(s[i])
            if d==0:
                x=1
            if d==numRows-1:
                x=-1

            d+=x
            i+=1
        a=""
        for i in ans:
            a+="".join(i)
        return a


        
      