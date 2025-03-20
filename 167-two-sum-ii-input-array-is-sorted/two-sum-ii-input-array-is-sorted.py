class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans.append(d.get(target-nums[i]))
                ans.append(i+1)
                break


            else:
                d[nums[i]]=i+1
      
        return ans

                
        