class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d={}
        l=0
        ans=0
        r=0
        while(r<len(s)):
            d[s[r]]=r

            if len(d)==3:
                ans+= (min(d.get('a'),d.get('b'),d.get('c'))+1)
            r+=1
        return ans




       