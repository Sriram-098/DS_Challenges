class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        def generate(i,sub,target,used):
            if target==0:
                result.append(sub[:])
                return 
            if i==len(nums):
                if target==0:
                    result.append(sub[:])
                return 
                


            for j in range(i,len(nums),1):

                
                if j>i and nums[j]==nums[j-1] :
                    continue
                if nums[j]>target:
                    break
                
                if nums[j]<=target:
                    used[j]=1
                    sub.append(nums[j])
                    generate(j+1,sub,target-nums[j],used)
                    sub.pop()
                    used[j]=0

                
        used=[0]*len(nums)
        generate(0,[],target,used)
        return result

        