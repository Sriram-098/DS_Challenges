class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l=0
        r=0
        maxi=0
        maxfreq=0
        while r<len(s):
            d[s[r]]=d.get(s[r],0)+1
            # print(d)
            maxfreq=max(d.values())
            
            while ((r-l+1)-maxfreq)>k:
                d[s[l]]=d.get(s[l])-1
                if d[s[l]]==0:
                    del d[s[l]]

                maxfreq=max(d.values())
                l+=1


            maxi=max(r-l+1,maxi)
            r+=1
        return maxi



         
        