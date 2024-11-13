from alpaca_trader import Alpacatrader 
from portfolio import Portfolio
from stock_frame import StockFrame

def main(): 

    #-------------------- TEST CASE 1: Creating an Alpaca Session--------------------------------

    # client_id = ''
    # secret_key = ''
    # alpaca_trader = Alpacatrader(client_id=client_id, secret_key=secret_key)

    # print("Alpaca Session Created: ", alpaca_trader.session)

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

    

    data = {
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
    print("DataFrame after adding a row:\n", df.frame)



if __name__ == "__main__":
    main()
        