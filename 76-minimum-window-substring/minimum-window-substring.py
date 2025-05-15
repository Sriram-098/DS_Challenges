class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=Counter(t)
        l=0
        r=0
        maxlen=1e9
        x=len(t)
        si=-1
        count=0
        while(r<len(s)):
            if s[r] in d and d[s[r]]>0:
                d[s[r]]-=1
                count+=1
            else :
                d[s[r]]=d.get(s[r],0)-1
            
            while(count==len(t)):
                if (r-l+1)<maxlen:
                    maxlen=r-l+1
                    si=l
                
                d[s[l]]+=1
                if d[s[l]]>0:
                    count-=1
                l+=1
            r+=1
        #print(s[si:si+maxlen])
        return "" if si==-1 else s[si:(si+maxlen)]

            

            




                


        