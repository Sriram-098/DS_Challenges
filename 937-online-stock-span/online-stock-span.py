class StockSpanner:

    def __init__(self):
        self.st=[]
        self.i=0 
        

    def next(self, price: int) -> int:
       
        while self.st and price >=self.st[-1][0]:
            self.st.pop()
        span=0
        if not self.st:
            span=self.i+1
        else:
            span=self.i-self.st[-1][1]

        self.st.append((price,self.i))
        self.i+=1
        return span
        
        
        


        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)