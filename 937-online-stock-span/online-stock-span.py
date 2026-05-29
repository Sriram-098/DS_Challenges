class StockSpanner:

    def __init__(self):
        # The stack will store tuples of: (price, span)
        self.st = [] 

    def next(self, price: int) -> int:
        # Every day starts with a base span of 1 (the day itself)
        span=1
        while self.st and price>=self.st[-1][0]:
            span+=self.st.pop()[1]

        self.st.append((price,span))
        
        return span