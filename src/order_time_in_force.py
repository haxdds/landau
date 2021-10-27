from enum import Enum

class OrderTimeInForce(Enum):
    """Time in Force (ToF) of the orderSS"""
    GTC = 0, # Only GTC and DAY supported
    DAY = 1,  
    FOK = 2,