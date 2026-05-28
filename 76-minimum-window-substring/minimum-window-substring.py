class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        d=Counter(t)
        maxi=1e9
        st=-1
        count=0
        while r<len(s):
            if s[r] in d and d[s[r]]>0:
                count+=1
                d[s[r]]-=1

            else:
                d[s[r]]=d.get(s[r],0)-1
            
            while count==len(t):
                if r-l+1<maxi:
                    maxi=r-l+1
                    st=l

                d[s[l]]+=1
                if d[s[l]]>0:
                    count-=1
                
                l+=1
            r+=1

        return s[st:st+maxi] if maxi!=1e9 else ""


            


            


        