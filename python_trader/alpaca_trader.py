#This is where we will be interacting with Alpaca API.
#Creating other objects

import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union 

from alpaca_trade_api.stream import Stream

class Alpacatrader():
    
    """This method runs when the object is initialized"""
    def __init__(self, client_id: str, secret_key: str, symbol: str) -> None:
        """_summary_

        Args:
            client_id (str): Client_Id to connect to AlpacaAPI
            secret_key (str): Use for authentication and refreshing the tokens
            base_url (str, optional): . Defaults to None.
            trading_account (str, optional): Help us determine where are we going to place those trades. Defaults to None.
        """        
    
        self.client_id: str = client_id
        self.secret_key: str = secret_key
        self.symbol: str = symbol
        self.session = self._create_session()
        self.stream = Stream(self.client_id, self.secret_key, base_url="wss://stream.data.alpaca.markets/v1beta1/crypto", raw_data=True)
   

    def _create_session(self) -> REST:
        """_summary_
        Creates a new authenticated session with Alpaca API. 

        Returns: A REST Client Object with an authenticated session 
        """    
        alpaca_client = REST(
            key_id=self.client_id,
            secret_key=self.secret_key,
            base_url="https://paper-api.alpaca.markets"
        )

        return alpaca_client
    
    async def print_quote(self, q):
        """Callback to print incoming quote data."""
        print('quote', q)

    async def print_trade(self, t):
        """Callback to print incoming trade data."""
        print('trade', t)

    async def print_bar(self, bar):
        """Callback to print incoming bar data."""
        print('bar', bar)

    def start_streaming(self): 

        self.stream.subscribe_crypto_quotes(self.print_quote, self.symbol)
        self.stream.subscribe_crypto_trades(self.print_trade, self.symbol)

        '''# Subscribe to bars
        @self.stream.on_bar(self.symbol)
        async def on_bar(bar):
            print('bar', bar)'''

        self.stream.subscribe_crypto_bars(self.print_bar, self.symbol)

        # Run the stream
        self.stream.run()
    

    

 #---------------------------------------------------------------
    
@property
def pre_market_open(self) -> bool:
        """Checks if pre-market is open.

        Uses the datetime module to create US Pre-Market Equity hours in
        UTC time.

        Usage:
        ----
            >>> trading_robot = PyRobot(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            credentials_path=CREDENTIALS_PATH
            )
            >>> pre_market_open_flag = trading_robot.pre_market_open
            >>> pre_market_open_flag
            True

        Returns:
        ----
        bool -- True if pre-market is open, False otherwise.

        """

        pre_market_start_time = datetime.utcnow().replace(
            hour=8,
            minute=00,
            second=00
        ).timestamp()

        market_start_time = datetime.utcnow().replace(
            hour=13,
            minute=30,
            second=00
        ).timestamp()

        right_now = datetime.utcnow().timestamp()

        if market_start_time >= right_now >= pre_market_start_time:
            return True
        else:
            return False

@property
def post_market_open(self):
        """Checks if post-market is open.

        Uses the datetime module to create US Post-Market Equity hours in
        UTC time.

        Usage:
        ----
            >>> trading_robot = PyRobot(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            credentials_path=CREDENTIALS_PATH
            )
            >>> post_market_open_flag = trading_robot.post_market_open
            >>> post_market_open_flag
            True

        Returns:
        ----
        bool -- True if post-market is open, False otherwise.

        """

        post_market_end_time = datetime.utcnow().replace(
            hour=00,
            minute=00,
            second=00
        ).timestamp()

        market_end_time = datetime.utcnow().replace(
            hour=20,
            minute=00,
            second=00
        ).timestamp()

        right_now = datetime.utcnow().timestamp()

        if post_market_end_time >= right_now >= market_end_time:
            return True
        else:
            return False

@property
def regular_market_open(self):
        """Checks if regular market is open.

        Uses the datetime module to create US Regular Market Equity hours in
        UTC time.

        Usage:
        ----
            >>> trading_robot = PyRobot(
            client_id=CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            credentials_path=CREDENTIALS_PATH
            )
            >>> market_open_flag = trading_robot.market_open
            >>> market_open_flag
            True

        Returns:
        ----
        bool -- True if post-market is open, False otherwise.

        """

        market_start_time = datetime.utcnow().replace(
            hour=13,
            minute=30,
            second=00
        ).timestamp()

        market_end_time = datetime.utcnow().replace(
            hour=20,
            minute=00,
            second=00
        ).timestamp()

        right_now = datetime.utcnow().timestamp()

        if market_end_time >= right_now >= market_start_time:
            return True
        else:
            return False

    
def generate_portfolio(self):
     pass

def generate_trade(self): 
     pass

def get_current_quotes(self) -> dict:
     pass

def get_historical_prices(self) -> List[Dict]:
     pass

def create_stock_frame(self):
     pass




