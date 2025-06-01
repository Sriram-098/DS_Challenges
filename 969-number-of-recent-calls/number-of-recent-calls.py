class RecentCounter:

    def __init__(self):
        self.ls=deque()
        

    def ping(self, t: int) -> int:
        self.ls.append(t)
        if len(self.ls)==0:
            return None

        if len(self.ls)==1:
            return 1

        while True:
            while self.ls and  t-self.ls[0]>3000:
                self.ls.popleft()

            if t-self.ls[0]<=3000:
                break

        return len(self.ls)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)