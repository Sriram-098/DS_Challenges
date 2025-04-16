class Solution:
    def numSplits(self, s: str) -> int:
        left={}
        right=Counter(s)
        count=0

        for i in s:
            if i in left:
                left[i]+=1
            else:
                left[i]=1
            
            right[i]-=1
            if right[i]==0:
                del right[i]

            if len(left)==len(right):
                count+=1
        return count
        