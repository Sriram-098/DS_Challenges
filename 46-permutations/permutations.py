class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[] 

        def swap(i,j,nums):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        def f(i,nums):
            if i==len(nums):
                ans.append(nums[:])
                return 
            for j in range(i,len(nums)):
                swap(i,j,nums)
                f(i+1,nums)
                swap(i,j,nums)

        f(0,nums)
        return ans
        








        