class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=dict()
        l=0
        r=0
        count=0
        while(r<len(s)):
            d[s[r]]=r

            if(len(d)==3):
                smallindex=min(d.get('a'),d.get('b'),d.get('c'))
                count=count+1+smallindex
            r+=1
        return count



        