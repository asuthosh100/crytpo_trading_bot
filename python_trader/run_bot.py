from alpaca_trader import Alpacatrader 
from portfolio import Portfolio
from stock_frame import StockFrame
from alpaca_historical_data import AlpacaHistData
from alpaca_websocket_usage import AlpacaWebsocket
from alpaca.data.live import CryptoDataStream

def main(): 

    #-------------------- TEST CASE 1: Creating an Alpaca Session--------------------------------

    '''API_KEY = ''
    SECRET_KEY = ''
    symbol = 'BTC/USD'
    alpaca_trader = Alpacatrader(client_id=API_KEY, secret_key=SECRET_KEY,symbol=symbol)
    print("Alpaca Session Created: ", alpaca_trader.session) 
    #alpaca_trader.start_streaming()

    stream = CryptoDataStream(
    api_key=API_KEY,
    secret_key=SECRET_KEY,
    )

    async def handler(data):
        print(data)
    
    stream.subscribe_quotes(handler, symbol)
    stream.subscribe_trades(handler, symbol)

    stream.run()'''

    #-------------------- TEST CASE 2: Creating a Portfolio Object, Adding and Deleting Positions--------------------------------

    #portfolio = Portfolio()

    #positions = [
    #{"symbol": "GOOGL", "asset_type": "Equity", "quantity": 5, "purchase_price": 2800.0, "purchase_date": "2024-10-15"},
    #{"symbol": "TSLA", "asset_type": "Equity", "quantity": 3, "purchase_price": 700.0, "purchase_date": "2024-11-01"}
#]
    
    #portfolio.add_positions(positions)
    #print(portfolio.positions)


    #portfolio.remove_postion('TSLA')
    #print(portfolio.positions)

    #------------------------------ TEST CASE 3: Testing Data_Frame--------------------------------

    """data = {
                "datetime": 1586390396750,
                "symbol": "MSFT",
                "close": 165.7,
                "open": 165.67,
                "high": 166.67,
                "low": 163.5,
                "volume": 48318234
            }
    
    df = StockFrame(data = data)
    print("Initial DataFrame:\n", df.frame)

    new_data = [{ 

        "datetime": 1576390396750,
        "symbol": "APPL",
        "close": 185.7,
        "open": 195.67,
        "high": 196.67,
        "low": 163.5,
        "volume": 48518234
    }
    ]
    
    df.add_row(new_data)
    print("DataFrame after adding a row:\n", df.frame)"""

    #------------------------------ TEST CASE 4: Requesting Historical Crypto Data from Alpaca--------------------------------
    symbol = "BTC/USD"
    #start_date = "2022-09-01"
    #end_date = "2022-09-07"
    
    # Create an instance of the AlpacaHistData class
    data = AlpacaHistData(symbol)
    
    # Access and print the DataFrame returned by the request
    print(data.request_param)

    #------------------------------ TEST CASE 4: Requesting Real Time Crypto Data from Alpaca--------------------------------


if __name__ == "__main__":
    main()
        