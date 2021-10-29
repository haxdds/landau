from alpaca_broker import AlpacaBroker
from alpaca_trade_api.rest import TimeFrame

alpaca = AlpacaBroker(live=False)

x = alpaca.connection.get_bars('SPY', TimeFrame.Day, '2021-01-01', '2021-10-01')





