class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,path):
            if len(path)==k:
                if sum(path)==n:
                    ans.append(path[:])
                return 

            for i in range(start,10):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
            




        backtrack(1,[])
        return ans
        