from order_type import OrderType
from order_time_in_force import OrderTimeInForce
from order_status import OrderStatus

class Order:

    def __init__(
        self,
        symbol:str,
        type: OrderType,
        quantity: float,
        time_in_force: OrderTimeInForce,
        limit_price: float=None,
        stop_price:float=None
    ):
        
        self.symbol = symbol
        self.type = type
        self.quantity = quantity
        self.time_in_force = time_in_force
        self.limit_price = limit_price
        self.stop_price = stop_price

        self.status = OrderStatus.NEW
        self.filled_quantity = 0
        
        self.time_submitted = None # needs to be implemented?
        self.time_filled = None

    

