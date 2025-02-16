class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        curr=0
        maxi=0
        s=list(s)
        dp=[1]*len(s)
        if(len(s)==1 and k==1):
            return True
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                dp[i]+=dp[i-1]
        print(dp)
        for i in range(0,len(s)):
            if(dp[i]==k and (i==len(s)-1 or dp[i+1]!=k+1)):
                return True
        return False

            
     
        
        