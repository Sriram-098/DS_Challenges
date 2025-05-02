class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum=0
        d={0:-1}
        for i in range(len(nums)):
            sum+=nums[i]
            rem=sum%k
            if rem in d:
                if i-d[rem]>1:
                    return True
            else:
                d[rem]=i

        return False

        



        