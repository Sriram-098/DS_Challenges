class Solution:
    def countBits(self, n: int) -> List[int]:
        result=[0]
        for i in range(1,n+1):
            count=0
            for j in range(32):
                if i&1==1:
                    count+=1
                i>>=1
            result.append(count)
        return result

        