class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        maxi=max(d.values())
        for i in range(len(nums)):
            if d.get(nums[i])==maxi:
                return nums[i]

        



        



            
        