from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

class AlpacaHistData(): 

    def __init__(self, symbol: str):
        self.client = CryptoHistoricalDataClient()
        self.symbol: str = symbol
        #self.start_date: str = start_date
        #self.end_date: str = start_date
        #self.start_date, self.end_date = self._date_range()
        self.request_param = self.create_request_param_and_request()
        


    '''def _date_range(self): 
        start_date: str = datetime.strptime(self.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(self.end_date, "%Y-%m-%d")
        return start_date, end_date'''


# Create the request parameters

    def create_request_param_and_request(self): 
    
        request_params = CryptoBarsRequest(
        symbol_or_symbols=[self.symbol],
        timeframe=TimeFrame.Day,
        start="2022-09-01",
        end="2022-09-07"
    )
        print("Requesting data with parameters:")
        print(f"Symbol: {self.symbol}")
        print(f"Timeframe: {TimeFrame.Day}")
        print(f"Start date: 2022-09-01")
        print(f"End date: 2022-09-07")

        btc_bars = self.client.get_crypto_bars(request_params)

        print("API response received:", btc_bars)

        if btc_bars.df.empty:
            print("No data available for the given symbol and date range.")
        return btc_bars.df
    
    

        
