class ProductOfNumbers:

    def __init__(self):
        self.ls=[1]
        
        

    def add(self, num: int) -> None:
        if num==0:
            self.ls=[1]
        else:
            self.ls.append(self.ls[-1]*num) if self.ls else self.ls


    def getProduct(self, k: int) -> int:
        if k>=len(self.ls):
            return 0
        else :
            return self.ls[-1]//self.ls[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)