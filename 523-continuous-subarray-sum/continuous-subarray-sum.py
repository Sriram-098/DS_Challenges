class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        d={0:-1}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k
            if rem in d:
                if i-d[rem]>1:
                    return True
            else:
                d[rem]=i
        return False

        