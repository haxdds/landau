from abc import ABC, abstractmethod
from datetime import datetime
from data_resolution import DataResolution
from pandas import DataFrame
from typing import List

class MarketDataVendor(ABC):
    """Abstract class for data vendor connections"""
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_historical_bars(
        self,
        symbol: str,
        start_date: datetime,
        end_date: datetime,
        resolution: DataResolution
    ) -> DataFrame:
        pass
    
    @abstractmethod
    def get_historical_bars(
        self, 
        symbols: List[str], 
        start_date: datetime, 
        end_date: datetime, 
        resolution: DataResolution
    ) -> DataFrame:
        pass
    
    @abstractmethod
    def get_historical_quotes(
        self, 
        symbol: str, 
        start_date: datetime, 
        end_date: datetime, 
        resolution: DataResolution=None
    ) -> DataFrame:
        pass

    @abstractmethod
    def get_historical_quotes(
        self, 
        symbols: List[str], 
        start_date: datetime, 
        end_date: datetime, 
        resolution: DataResolution=None
    ) -> DataFrame:
        pass