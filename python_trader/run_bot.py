from alpaca_trader import Alpacatrader 
from portfolio import Portfolio

def main(): 

    # client_id = ''
    # secret_key = ''
    # alpaca_trader = Alpacatrader(client_id=client_id, secret_key=secret_key)

    # print("Alpaca Session Created: ", alpaca_trader.session)

    portfolio = Portfolio()

    positions = [
    {"symbol": "GOOGL", "asset_type": "Equity", "quantity": 5, "purchase_price": 2800.0, "purchase_date": "2024-10-15"},
    {"symbol": "TSLA", "asset_type": "Equity", "quantity": 3, "purchase_price": 700.0, "purchase_date": "2024-11-01"}
]
    
    portfolio.add_positions(positions)
    print(portfolio.positions)


    portfolio.remove_postion('TSLA')
    print(portfolio.positions)


if __name__ == "__main__":
    main()
        