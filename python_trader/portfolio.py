from typing import List
from typing import Dict
from typing import Union 

from typing import Optional

class Portfolio():

    def __init__(self): 
        self.positions = {}
        self.positions_count = 0
        self.market_value = 0.0 
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        #self.account_number = account_num

    def add_position(self, symbol :str, asset_type: str,  purchase_date: Optional[str], quantity: int = 0, purchase_price: float = 0.0) -> dict:
        """_summary_

        This method adds a new position to the portfolio
        Each position stores details like quantity, purchase price, purchase date, and asset type.

        Args:
            symbol (str): Symbol of the financial instrument
            asset_type (str): eg. 'Equity', 'Options', 'futures'
            purchase_data (Optional[str]): _description_
            quantity (int, optional): _description_. Defaults to 0.
            purchase_price (float, optional): _description_. Defaults to 0.0.
        """        

        self.positions[symbol] = {}
        self.positions[symbol]['symbol'] = symbol
        self.positions[symbol]['quantity'] = quantity
        self.positions[symbol]['purchase_price'] = purchase_price
        self.positions[symbol]['purchase_date'] = purchase_date
        self.positions[symbol]['asset_type'] = asset_type

        return self.positions[symbol]
    
    def add_positions(self, positions: List[dict]) -> dict:
        
        if isinstance(positions, list): 
            for position in positions:
                 self.add_position(
                    symbol = position['symbol'],
                    asset_type = position['asset_type'],
                    quantity = position.get('quantity', 0),
                    purchase_price = position.get('purchase_price', 0.0),
                    purchase_date = position.get('purchase_date', None)
                )

            return self.positions

        else:
            raise TypeError('Positions must be a list of dictionaries.')

    def remove_postion(self, symbol: str)-> tuple[bool, str]: 
        if symbol in self.positions:
            del self.positions[symbol]
            return (True,"{symbol} was successfully removed.".format(symbol=symbol))
        else :
             return (False,"{symbol} doesnt exist.".format(symbol=symbol))
        

    def present_in_portfolio(self, symbol:str) -> bool:

        if symbol in self.positions_count:
            return True
        
        else :
            return False
        
    def profitable(self, symbol: str,  current_price: float = 0.0 ) -> bool: 

        purchase_price = self.positions[symbol]['purchase_price']
        if(purchase_price < current_price):
            return True
        else :
            return False