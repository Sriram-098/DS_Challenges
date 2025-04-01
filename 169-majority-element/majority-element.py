class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=Counter(nums)
        maxi=max(x.values())
        for i in range(len(nums)):
            if x.get(nums[i])==maxi:
                return nums[i]
        return -1
        