from alpaca import Alpaca
from alpaca_trade_api.rest import TimeFrame

alpaca = Alpaca(live=False)

x = alpaca.connection.get_bars('SPY', TimeFrame.Day, '2021-01-01', '2021-10-01')



