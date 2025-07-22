class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        d={}
        def f(i,j,k):
            if i==len(s1) and j==len(s2) and k==len(s3):
                return True
            if k==len(s3):
                return False
            if (i,j,k) in d:
                return d[(i,j,k)]
            first=False
            second=False
            if i<len(s1) and s1[i]==s3[k]:
                first=f(i+1,j,k+1)
            if j<len(s2) and s2[j]==s3[k]:
                second=f(i,j+1,k+1)
            d[(i,j,k)]=first or second
            
            return d[(i,j,k)]



        if len(s1)+len(s2)!=len(s3):
            return False
        
        return f(0,0,0)
        