class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        def generate(i,sub,target):
            if i==len(nums):
                if target==0:
                    result.append(sub[:])
                return 
            if target==0:
                result.append(sub[:])
                return 
            if nums[i]>target:
                return

            if nums[i]<=target:
                sub.append(nums[i])
                generate(i,sub,target-nums[i])
                sub.pop()

            generate(i+1,sub,target)

        generate(0,[],target)
        return result




        