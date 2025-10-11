class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def f(i):
            if i==len(nums):
                result.append(nums[:])
                return 

            for j in range(i,len(nums),1):
                nums[i],nums[j]=nums[j],nums[i]
                f(i+1)
                nums[i],nums[j]=nums[j],nums[i]


        f(0)
        return result

        