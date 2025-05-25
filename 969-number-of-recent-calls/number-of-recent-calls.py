class RecentCounter:

    def __init__(self):
        self.ls=[]
        

    def ping(self, t: int) -> int:
        self.ls.append(t)
        if len(self.ls)==0:
            return None
        if len(self.ls)==1:
            return 1
        ind=0
        for i in range(len(self.ls)-1,-1,-1):
            if t-self.ls[i]>3000:
                ind=i+1
                break
                
        print(len(self.ls),ind)
        return len(self.ls)-ind
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)