from abc import ABC, abstractmethod
from datetime import datetime
from time_frame import TimeFrame

class DataVendor(ABC):
    """Abstract class for data vendor connections"""
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_historical_bar(self, symbol: str, start_date: datetime, end_date: datetime, resolution: TimeFrame):
        pass
    
    @abstractmethod
    def get_historical_bars(self, symbols: str, start_date: datetime, end_date: datetime, resolution: TimeFrame):
        pass
    
    @abstractmethod
    def get_historical_quote(self, symbol: str, start_date: datetime, end_date: datetime, resolution: TimeFrame=None):
        pass

    @abstractmethod
    def get_historical_quotes(self, symbols: str, start_date: datetime, end_date: datetime, resolution: TimeFrame=None):
        pass