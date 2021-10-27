from enum import Enum

class OrderStatus(Enum):
    """States an order can take"""
    NEW = 0,
    PARTIALLY_FILLED = 1,
    FILLED = 2,
    PENDING_CANCELED = 3,
    CANCELED = 4

