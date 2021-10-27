import os
from dotenv import load_dotenv;
import alpaca_trade_api;

load_dotenv();

class AlpacaBroker:
    
    def __init__(self, live=False):
        self.live = live

        endpoint = os.getenv('ALPACA_LIVE_ENDPOINT') if live else os.getenv('ALPACA_PAPER_ENDPOINT')

        self.connection = alpaca_trade_api.REST(os.getenv('ALPACA_API_KEY'), os.getenv('ALPACA_API_SECRET'), endpoint)

    
    @property
    def is_live(self):
        return self.is_live;
        





