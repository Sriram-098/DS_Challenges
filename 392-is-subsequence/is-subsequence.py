class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        j=0
        for i in range(len(t)):
            if s[j]==t[i]:
                j+=1
            if j==len(s):
                return True
        return False
            
        