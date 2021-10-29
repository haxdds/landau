import os
from market_data_vendor import MarketDataVendor
from alpaca_trade_api.rest import TimeFrame, REST
from dotenv import load_dotenv;
from datetime import datetime
from data_resolution import DataResolution
from globals import *

load_dotenv()

class AlpacaVendor(MarketDataVendor):

    def __init__(self, name='Alpaca'):
        super().__init__(name)
        
        self.alpaca = REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_API_SECRET'), "https://data.alpaca.markets/v2")

    def get_historical_bar(self, symbol: str, start_date: datetime, end_date: datetime, resolution: DataResolution):
        
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        if resolution == DataResolution.Minute:
            tf = TimeFrame.Minute
        elif resolution == DataResolution.Hour:
            tf = TimeFrame.Hour
        else:
            tf = TimeFrame.Day


        return self.alpaca.get_bars(symbol, tf, start_date_str, end_date_str).df


    def get_historical_quote(self, symbol: str, start_date: datetime, end_date: datetime, resolution: DataResolution = None):
        return super().get_historical_quote(symbol, start_date, end_date, resolution=resolution)


    def get_historical_bars(self, symbols: str, start_date: datetime, end_date: datetime, resolution: DataResolution):
        return super().get_historical_bars(symbols, start_date, end_date, resolution)

    def get_historical_quotes(self, symbols: str, start_date: datetime, end_date: datetime, resolution: DataResolution = None):
        return super().get_historical_quotes(symbols, start_date, end_date, resolution=resolution)
