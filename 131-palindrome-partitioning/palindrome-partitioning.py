class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def f(start,sub):
            if start==len(s):
                result.append(sub[:])
                return


            for end in range(start,len(s)):
                if s[start:end+1]==s[start:end+1][::-1]:
                    sub.append(s[start:end+1])
                    f(end+1,sub)
                    sub.pop()



        f(0,[])
        return result




        
        