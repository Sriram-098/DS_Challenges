class Solution:
   
    def subsetXORSum(self, nums: List[int]) -> int:
        s=0
        sub=[]
        
        return self.f(0,sub,s,nums)

    def f(self,i,sub,s,nums):
        
        if i>=len(nums):
            a=0
            for j in range(len(sub)):
                a=a^sub[j]

            return a
            
            
            



        sub.append(nums[i])
        x=self.f(i+1,sub,s,nums)
        sub.pop()
        y=self.f(i+1,sub,s,nums)

        return x+y
        