class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=Counter(s1)
        x=len(s1)
        r=0
        while(r<len(s2)):
            if r+x<=len(s2) and a==Counter(s2[r:r+x]):
                return True

            r+=1
        return False