import os
from data_vendor import DataVendor
import alpaca_trade_api as api
from alpaca_trade_api.rest import TimeFrame
from dotenv import load_dotenv;
from datetime import datetime
from data_resolution import DataResolution

class AlpacaVendor(DataVendor):

    def __init__(self, name='Alpaca'):
        super().__init__(name)
        self.alpaca = api.REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_API_SECRET'))


    def get_historical_bar(self, symbol: str, start_date: datetime, end_date: datetime, resolution: DataResolution):
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")
        tf = TimeFrame(resolution.amount, resolution.unit)

        return self.alpaca.get_bars(symbol, start_date_str, end_date_str, tf)


    def get_historical_quote(self, symbol: str, start_date: datetime, end_date: datetime, resolution: DataResolution = None):
        return super().get_historical_quote(symbol, start_date, end_date, resolution=resolution)


    def get_historical_bars(self, symbols: str, start_date: datetime, end_date: datetime, resolution: TimeFrame):
        return super().get_historical_bars(symbols, start_date, end_date, resolution)

    def get_historical_quotes(self, symbols: str, start_date: datetime, end_date: datetime, resolution: DataResolution = None):
        return super().get_historical_quotes(symbols, start_date, end_date, resolution=resolution)
