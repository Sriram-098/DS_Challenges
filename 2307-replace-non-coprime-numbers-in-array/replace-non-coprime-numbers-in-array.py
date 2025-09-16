from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a,b):
            return a*b //gcd(a,b)
            
        st=[]
        for num in nums:
            st.append(num)
            while len(st)>1 and gcd(st[-1],st[-2])>1:
                a=st.pop()
                b=st.pop()
                st.append(lcm(a,b))
        return st

            
        



        