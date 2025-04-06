class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows==len(s):
            return s

        lis=[[] for _ in range(numRows)]
        ind=0
        d=0
        for char in s:
            lis[ind].append(char)
            if ind==0:
                d=1
            elif ind==numRows-1:
                d=-1

            ind+=d

        x=""

        for i in range(len(lis)):
            x+=''.join(lis[i])

        return x
      