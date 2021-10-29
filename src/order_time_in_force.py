from enum import Enum

class OrderTimeInForce(Enum):
    """Time in Force (ToF) of the orderss"""
    GTC = 0,  # good till cancelled
    DAY = 1,  # day
    FOK = 2,  # fill or kill