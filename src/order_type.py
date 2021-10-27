from enum import Enum

class OrderType(Enum):
    """Types of orders"""
    MARKET = 0,
    LIMIT = 1,
    STOP = 2