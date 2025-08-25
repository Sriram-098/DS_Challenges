
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        d={}
        def f(a,b):
            key=(a,b)
            if key in d:
                return d[key]
            if a==b:
                d[key]=True
                return True
            if sorted(a)!=sorted(b):
                d[key]=False
                return False
            
            for i in range(1,len(a)):
                if f(a[i:],b[i:]) and f(a[:i],b[:i]):
                    d[key]=True
                    return True
                if f(a[i:],b[:-i]) and f(a[:i],b[-i:]):
                    d[key]=True
                    return True
            d[key]=False
            return False


        return f(s1,s2)
        