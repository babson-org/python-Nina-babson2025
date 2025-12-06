
class Stock:
    def __init__(self, sym, name, shares=0.0, cost=0.0):
        """TODO:""" #assigns attributes from parameters
        self.sym = sym
        self.name = name
        self.shares = float(shares)
        self.cost = float(cost)


    def __str__(self):
        """TODO: include symbol, shares, and cost (format flexible).""" #want a string that symbol, shares, and cost displayed
        return f"{self.sym}: {self.shares} shares, cost ${self.cost}"
    
