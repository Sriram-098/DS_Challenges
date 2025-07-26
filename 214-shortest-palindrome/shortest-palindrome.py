class Solution:
    def shortestPalindrome(self, s: str) -> str:
        srev=s[::-1]
        x=s
        s=s+'*'+srev
        lps=[0]*(len(s)+1)
        i=1
        j=0
        while i<len(s):
            if s[i]==s[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        pali=lps[-2]
        print(lps)
        print(pali)
        st=srev[0:len(srev)-pali]
        print(st,x)
        ans=st+x
        return ans
        