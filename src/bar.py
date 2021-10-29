from data import Data
from datetime import datetime
class Bar(Data):

    def __init__(
        self, 
        symbol: str, 
        time: datetime, 
        open: float, 
        high: float, 
        low: float, 
        close: float, 
        volume: float=0, 
        exchange: str=''):
        
        super().__init__(symbol, time, close)

        self.exchange = exchange

        self.open = open
        self.high = high
        self.low = low

        self.volume = volume
        
        