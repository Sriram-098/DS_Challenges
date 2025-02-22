class Solution:
    def ishelper(self,sub,i,res,nums):
        if(i>=len(nums)):
            res.append(sub.copy())
            return
        
        sub.append(nums[i])
        self.ishelper(sub,i+1,res,nums)
        sub.remove(nums[i])
        self.ishelper(sub,i+1,res,nums)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        self.ishelper(sub,0,res,nums)
        return res

    
        
        