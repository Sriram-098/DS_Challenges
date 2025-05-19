class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t=0
        l=0
        b=len(matrix)-1
        r=len(matrix[0])-1
        lis=[]
        while(t<=b and l<=r):
            for i in range(l,r+1):
                lis.append(matrix[t][i])
            t+=1
            
            for i in range(t,b+1):
                lis.append(matrix[i][r])
            r-=1
            if(t<=b):
                for i in range(r,l-1,-1):
                    lis.append(matrix[b][i])
                b-=1
            if(l<=r):
                for i in range(b,t-1,-1):
                    lis.append(matrix[i][l])
                l+=1
        print(lis)
        return lis
        