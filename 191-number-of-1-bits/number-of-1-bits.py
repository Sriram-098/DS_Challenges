class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for _ in range(32):
            if n & 1==1:
                count+=1
            n=n>>1

        return count
        