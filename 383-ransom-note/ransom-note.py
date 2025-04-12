class Solution:
    def canConstruct(self, a: str, b: str) -> bool:
        x=Counter(a)
        y=Counter(b)

        for i in x.keys():
            if i in y:
                if x.get(i)<=y.get(i):
                    continue
                else:
                    return False
            else:
                return False

        return True
        
        