class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        imax=0
        total=0
        submax=0
        for i in range(len(nums)):
            total=max(total,submax*nums[i])
            submax=max(imax-nums[i],submax)
            imax=max(imax,nums[i])
        return total
        