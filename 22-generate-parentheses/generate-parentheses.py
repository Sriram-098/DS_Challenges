class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def f(left,right,s):
            if left==n and right==n:
                ans.append(s)
                return 

            if left<n:
                f(left+1,right,s+"(")
            if left >right:
                f(left,right+1,s+")")


        f(0,0,"")
        return ans
        