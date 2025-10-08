from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=Counter(t)
        le=len(d)
        l=0
        r=0
        count=0
        maxlength=1e9
        st=-1
        while r<len(s):
            
            if s[r] in d and d[s[r]]>0:
                count+=1
                d[s[r]]-=1
            else:
                d[s[r]]=d.get(s[r],0)-1
            #print(d)

            while count==len(t):
                if r-l+1<maxlength:
                    print(l)
                    st=l
                    maxlength=r-l+1
                
                d[s[l]]+=1
                if d[s[l]]>0:
                    count-=1

                l+=1
            r+=1
        print(l)
        return s[st:st+maxlength] if st!=-1 else ""



      

            

            




                


          
                

                
            
            

        