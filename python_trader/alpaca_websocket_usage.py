from alpaca_trade_api.stream import Stream


class AlpacaWebsocket():

    def __init__(self,symbol: str, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.symbol = symbol
        self.stream = Stream(self.api_key, self.secret_key, raw_data=True)

    async def print_quote(self, q):
        """Callback to print incoming quote data."""
        print('quote', q)

    async def print_trade(self, t):
        """Callback to print incoming trade data."""
        print('trade', t)

    def start_streaming(self): 

        self.stream.subscribe_crypto_quotes(self.print_quote, self.symbol)
        self.stream.subscribe_crypto_trades(self.print_trade, self.symbol)

        # Subscribe to bars
        @self.stream.on_bar(self.symbol)
        async def on_bar(bar):
            print('bar', bar)

        # Run the stream
        self.stream.run()