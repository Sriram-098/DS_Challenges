class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count=0
        g.sort()
        s.sort()
        j=0
        used=[0]*len(s)
        for i in range(len(g)):
            prev_count=count
            for j in range(len(s)):
                if s[j]>=g[i] and used[j]==0:
                    count+=1
                    used[j]=1
                    break
            if prev_count==count:
                break
            
                
        return count

        