class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                # Min is in the right half
                low = mid + 1
            else:
                # Min is in the left half including mid
                high = mid
        
        return nums[low]

        
        
        