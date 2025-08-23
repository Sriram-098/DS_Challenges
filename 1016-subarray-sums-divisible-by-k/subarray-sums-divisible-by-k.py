class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        s=0
        ans=0
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k
            ans+=d.get(rem,0)
            d[rem]=d.get(rem,0)+1
        return ans

        