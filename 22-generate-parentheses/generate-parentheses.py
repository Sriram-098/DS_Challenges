class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def f(left,right,s,count):
            if left==0 and right==0:
                ans.append(s)
                count+=1
                return 

            


            if left>=0:
                f(left-1,right,s+'(',count)

            if right>left:
                f(left,right-1,s+')',count)


        count=0
        f(n,n,"",count)
        print(count)

        return ans
        