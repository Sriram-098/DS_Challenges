class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        count=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            rem=(sum%k+k)%k
            count+=d.get(rem,0)
            d[rem]=d.get(rem,0)+1

        return count

        
        