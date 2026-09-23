class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count=0
        g.sort()
        s.sort()
        i=0
        j=0
        while j<len(s):
            if i<len(g) and s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count
           
            

            
        return count

        