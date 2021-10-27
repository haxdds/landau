from abc import ABC, abstractmethod
from order_type import OrderType
from order_time_in_force import OrderTimeInForce
from order import Order;

class Broker:

    def __init__(self, name: str, live: bool, market_open, market_close):
        self.name = name
        self.live = live
        self.market_open = market_open
        self.market_close = market_close

    @abstractmethod
    def submit_order(
        self,
        symbol:str,
        type: OrderType,
        quantity: float,
        time_in_force: OrderTimeInForce,
        limit_price: float=None,
        stop_price:float=None
    ) -> Order:

        pass

    @abstractmethod
    def submit_market_order(self, symbol: str, quantity: float) -> Order:
        pass