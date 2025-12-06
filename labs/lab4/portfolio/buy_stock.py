

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    # Check if symbol is valid in DOW 30 #
    if sym not in _prices.DOW30:
        print("Invalid Symbol")
    else:
        return

    # Validate Shares - must buy 1 or more shares #
    if shares <= 0:
        print("IYou must buy a minimum of 1 share")
    else:
        return
    
    # Check Price #
    if sym not in _prices.get_last_close_map([sym]):
        print("Price not found")
    else:
        return

    # Check if client has enough money #
    total_price = _prices.get_last_close_maplast_close_map[sym] * shares
    if total_price < self.cash:
        print("You do not have enough money in your account")
    else:
        total_price >= self.cash
        print("You have enough money!")
    
    # Update current position OR create new position #
    cur_pos = _find_position(self, sym) #for if client already has some shares of this company
    if cur_pos:
        cur_pos["share"] += shares
        cur_pos["cost"] += total_price

    new_cur_pos = {
        "sym": sym,
        "name": sym,
        "shares": shares,
        "cost": total_price
    }

    self.positions.append(new_cur_pos)

# Subtract cost from client account - display transaction #
self.cash -= total_price