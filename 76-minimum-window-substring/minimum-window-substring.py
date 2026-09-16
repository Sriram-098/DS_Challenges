class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=Counter(t)
        mini=1e9
        l=0
        r=0
        count=0
        ind=-1
        while r<len(s):
            if s[r] in d and d[s[r]]>0 :
                count+=1
                d[s[r]]-=1
            else:
                d[s[r]]=d.get(s[r],0)-1

            while count==len(t):
                if r-l+1<mini:
                    mini=r-l+1
                    ind=r
                d[s[l]]+=1
                if d[s[l]]>0:
                    count-=1
                l+=1

            r+=1
        return s[ind-mini+1:ind+1] if mini!=1e9 else ""

                
            
            
            


            