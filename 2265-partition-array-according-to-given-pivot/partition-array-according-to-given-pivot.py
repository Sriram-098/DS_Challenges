class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small_ele=[]
        large_ele=[]
        equal=[]
        for i in range(len(nums)):
            if nums[i]>pivot:
                large_ele.append(nums[i])
            elif (nums[i]<pivot):
                small_ele.append(nums[i])
            else:
                equal.append(nums[i])
        small_ele.extend(equal)
        small_ele.extend(large_ele)
        return small_ele
      
        