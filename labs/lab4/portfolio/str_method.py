
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56" #positions is number of stocks the person owns
    """

    return f"{self.client}: has {self.shares} positions with a balance of ${self.cash} cash"

portfolio_str("David")
