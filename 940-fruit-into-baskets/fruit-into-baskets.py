class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen=dict()
        l=0
        r=0
        maxlen=0
        while(r<len(fruits)):
            seen[fruits[r]]=seen.get(fruits[r],0)+1
            while(len(seen)>2):
                
                seen[fruits[l]]-=1
                if seen.get(fruits[l])==0:
                    del seen[fruits[l]]
                l+=1
            
            if len(seen)<=2:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

        