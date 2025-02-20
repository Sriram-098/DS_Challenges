class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        ans=[]
        x=[]
        n=len(nums[0])
        def backtrack():
            if len(x)==n:
                y="".join(x)
                
                if(y not in nums):
                    ans.append("".join(x))
                return 
            for i in range(2):
                x.append(str(i))
                backtrack()
                if ans:
                    return 
                x.pop()
        backtrack()
        return ans[0] if ans else ""
    

            

        