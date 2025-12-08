
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    # Check if symbol exists #
    cur_pos = _find_position(self, sym)
    if cur_pos not in self.positions:
        print("Shares not available")
        return #early exit on error
    
    # Ensure shares <= owned shares
    if cur_pos["shares"] < shares:
        print("Insufficient shares available")
    elif cur_pos["shares"] >= shares:
        print("Suffient shares to sell")
        return
    
    # Check Price #
    if sym not in _prices.get_last_close_map([sym]):
        print("Price not found")
        return
    
    # Reduce position shares; adjust 'cost' proportionally by shares. (assumes average cost accounting) #
    cur_pos["shares"] -= shares
    cost_per_share = cur_pos["cost"] / cur_pos["share"]
    cost_reduction = cost_per_share * shares
    self.cash += shares*price
    # If shares = 0, remove share
    if cur_pos["shares"] == 0:
        self.position.remove(cur_pos) #if position = 0, the symbol is also taken out of the client portfolio

    print(f"Congrats! You sold {shares} shares of {sym}")