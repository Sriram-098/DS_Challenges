class Solution:
    def minWindow(self, s: str, p: str) -> str:
        d=Counter(p)
        #print(d)
        ind=-1
        mini=1e9
        l=0
        r=0
        count=0
        while r<len(s):
            if d[s[r]]>0:
                d[s[r]]-=1
                count+=1
            else:
                if s[r] in d:
                    d[s[r]]-=1
                else:
                    d[s[r]]=-1
                
            while count==len(p) :
                print(l,r,count)
                leng=r-l+1
                if leng<mini:
                    ind=l
                    mini=r-l+1
                
                d[s[l]]+=1
                if d[s[l]] >0:
                    count-=1
                
        
                l+=1
            
            r+=1
                
        return s[ind:(ind+mini)] if ind!=-1 else ""
                    
                    
            
            
    
        
        