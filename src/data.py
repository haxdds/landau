from abc import ABC
from datetime import datetime
from typing import Any


class Data(ABC):

    def __init__(self, symbol: str, time: datetime, value: Any):
        self.symbol = symbol
        self.time = time
        self.value = value