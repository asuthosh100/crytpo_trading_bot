from alpaca_trader import Alpacatrader 

def main(): 

    client_id = 'PKVUX2M5K5YZWCK8E2JN'
    secret_key = 'iK5aTBDK0VRjaVSTjeZHaqHMPbMCndkWNYrh9Hcl'
    alpaca_trader = Alpacatrader(client_id=client_id, secret_key=secret_key)

    print("Alpaca Session Created: ", alpaca_trader.session)



if __name__ == "__main__":
    main()
        