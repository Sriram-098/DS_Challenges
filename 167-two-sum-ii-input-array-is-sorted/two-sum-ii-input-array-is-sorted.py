class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        ans=[]
        while(l<r):
            if nums[l]+nums[r]<target:
                l+=1
            elif nums[l]+nums[r]>target:
                r-=1

            else:
                ans.append(l+1)
                ans.append(r+1)
                break
        
        return ans
        

                
        