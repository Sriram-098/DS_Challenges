class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref=0
        d={0:1}
        count=0
        for i in range(len(nums)):
            pref+=nums[i]
            rem=pref%k
            count+=d.get(rem,0)
            d[rem]=d.get(rem,0)+1

        return count

        