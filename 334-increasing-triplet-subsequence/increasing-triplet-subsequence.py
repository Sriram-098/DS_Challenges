class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first=float('inf')
        second=float('inf')

        for i in range(len(nums)):
            if nums[i]<=first:
                first=nums[i]
            elif nums[i]<=second:
                second=nums[i]
            else:
                return True
            
        return False
        
        