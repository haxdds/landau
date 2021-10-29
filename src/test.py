from alpaca_broker import AlpacaBroker
from alpaca_vendor import AlpacaVendor
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime
from data_resolution import DataResolutionUnit

alpaca = AlpacaVendor("lucy")

a = datetime(2021, 10, 1)
b = datetime(2021, 10, 5)
f = DataResolutionUnit.Day

x = alpaca.get_historical_bar('SPY', a, b, f);

print(x)





