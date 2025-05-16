class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        maxsum=-1e9
        for i in nums:
            current_sum+=i
            if maxsum<current_sum:
                maxsum=current_sum
            if current_sum<0:
                current_sum=0

        return maxsum
        