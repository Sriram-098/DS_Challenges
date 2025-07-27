from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d=defaultdict()
        if not s:
            return True
        d[s[0]]=s
        
        print(d)
        for i in range(len(t)):
            if t[i] not in d:
                continue
            char=d[t[i]]
            del d[t[i]]
            if len(char[1:])==0:
                return True
            else :
                d[char[1]]=char[1:]
        return False
        
            
        