class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        count=0
        lis=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                lis.append(nums[i])
            else:
                count+=1
        a=[0]*count
        lis.extend(a)
        return lis
        

        