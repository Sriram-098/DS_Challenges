class Solution:
    def longestPrefix(self, s: str) -> str:
        lps=[0]*len(s)
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
        return s[0:lps[len(s)-1]]

        