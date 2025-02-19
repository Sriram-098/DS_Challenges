class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans=[]
        x=[]
        def backtrack():
            nonlocal k
            if len(x)==n:
                k-=1
                if k==0:
                    ans.append("".join(x))
                
                return 

            for i in range(3):
                s=chr(97+i)
                if len(x)==0 or x[-1]!=s:
                    x.append(s)
                    print(x)
                    backtrack()
                    if ans:
                        return 
                    x.pop()
        backtrack()
        return ans[0] if ans else ""
        
                

        


        
        