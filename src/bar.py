from base_data import BaseData

class Bar(BaseData):

    def __init__(self, time, open, high, low, close, volume=0, exchange=''):
        
        super().__init__(time, close)

        self.exchange = exchange

        self.open = open
        self.high = high
        self.low = low
        self.close = close

        self.volume = volume
        
        