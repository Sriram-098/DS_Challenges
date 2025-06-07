class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]

        def is_valid(x,path):
            if len(x)==0 or (len(x)>1 and x[0]=='0'):
                return False
            return 0<=int(x)<=255
            

        def backtrack(start,path):
            if len(path)==4:
                if "".join(path)==s:
                    ans.append(".".join(path))
                return 


            for i in range(start,len(s)):
                if is_valid(s[start:i+1],path):
                    path.append(s[start:i+1])
                    
                    backtrack(i+1,path)
                    path.pop()
                  



        backtrack(0,[])
        return ans





        