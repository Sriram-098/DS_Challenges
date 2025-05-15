class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h=[0]*26
        l=0
        r=0
        maxlen=0
        maxfre=0
        while(r<len(s)):
            h[ord(s[r])-ord('A')]+=1
            maxfre=max(h[ord(s[r])-ord('A')],maxfre)

            while((r-l+1)-maxfre >k):
                h[ord(s[l]) - ord('A')]-=1
                for i in range(26):
                    maxfre=max(maxfre,h[i])

                l+=1
            
            if((r-l+1)-maxfre <=k):
                maxlen=max(maxlen,(r-l+1))

            r+=1
        return maxlen
        