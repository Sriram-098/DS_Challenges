class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans=[]
        def generate(s,left,right):
            if left==n and right==n:
                ans.append(s)
                return 


            if left<n:
                generate(s+'(',left+1,right)
            if right<left:
                generate(s+')',left,right+1)



        generate("",0,0)
        return ans
        