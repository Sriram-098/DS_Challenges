from math import gcd 
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def lcm(num1,num2):
            return num1*num2//gcd(num1,num2)

        st=[]
        for i in range(len(nums)):
            st.append(nums[i])
            while len(st)>1 and gcd(st[-1],st[-2])>1:
                a=st.pop()
                b=st.pop()
                st.append(lcm(a,b))
        return st
            
            
        