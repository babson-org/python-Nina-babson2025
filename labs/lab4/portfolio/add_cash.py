
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
    if amount < 0:
        print("Negative balance not valid")
    elif amount == 0:
        print("Please enter amount: ")
    else:
        self.cash += amount
        print(f" ${amount} cash has been added to your account. Your updated balance is ${self.cash}")
    