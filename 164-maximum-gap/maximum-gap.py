class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxGap=0
        for i in range(1,len(nums)):
            maxGap=max(maxGap,nums[i]-nums[i-1])
        return maxGap
        