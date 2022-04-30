## :wave: Welcome to AlgoTrading

:point_right: Open source project dedicated to delivering high quality alpha
<br />
:point_right: Advanced, high performance backtesting engine
<br />
:point_right: Sponsored by Vicarisi Ventures, a quantitative development company
<br />
:point_right: To learn more, visit https://vicarisi.com/
<br />

### :raised_hand_with_fingers_splayed: Getting Started 

The general steps are as followed: 

1. Initialize the Client: Object contains API Details
2. Fetch Historical Data with Client
3. Initialize Backtesting Parameters: Indicator Specifications
4. Compute Backtesting Indicators: Statistical Model, and Volatility
5. Initialize Statistics: Object contains insightful statistics
6. Compute Backtest Results: Returns PnL and Statistics Object
7. Print Scalar Statistics to Terminal
8. Visual Results: Distribution, PnL, Volatility 

### :raised_hand_with_fingers_splayed: Initialize Client

```markdown
from Data.Client import Client

endpoint = "sandbox.tradier.com"
api_key = "ENTER API KEY"
accountid = "ENTER ACCOUNT ID"
ticker = "AAPL"
months = 60
client = Client(endpoint, api_key, accountid, ticker, months)
```

### :raised_hand_with_fingers_splayed: Fetch Historical Data
```markdown
from Data.Historical import get_historical_data

ohlc = get_historical_data(client)
```

### :raised_hand_with_fingers_splayed: Initialize Backtesting Parameters
```markdown
from Indicators.Parameters import Parameters

period = 20
projection = 0
par = Parameters(period, projection)
```

### :raised_hand_with_fingers_splayed: Compute Backtesting Indicators
```markdown

from Indicators.LeastSquares import get_least_squares

open = ohlc.open[period:]
high = ohlc.high[period:]
low = ohlc.low[period:]
close = ohlc.close[period:]

least_squares_average = get_least_squares(par, close)

```

### :raised_hand_with_fingers_splayed: Initialize Statistics
```markdown
from Backtesting.Statistics import Statistics

lot_size = 1
least_squares_open = Statistics(lot_size, len(open[period:]))
least_squares_high = Statistics(lot_size, len(high[period:]))
least_squares_low = Statistics(lot_size, len(low[period:]))
least_squares_close = Statistics(lot_size, len(close[period:]))
```

### :raised_hand_with_fingers_splayed: Compute Backtest Results
```markdown
from Backtesting.Backtest import get_vanilla_backtest

least_squares_open = get_vanilla_backtest(least_squares_open, open[period:], least_squares_average)
least_squares_high = get_vanilla_backtest(least_squares_high, high[period:], least_squares_average)
least_squares_low = get_vanilla_backtest(least_squares_low, low[period:], least_squares_average)
least_squares_close = get_vanilla_backtest(least_squares_close, close[period:], least_squares_average)
```

### :raised_hand_with_fingers_splayed: Print Statistics
```markdown
from HelperMethods.Helpers import print_results

stats_list = [least_squares_open, least_squares_high, least_squares_low, least_squares_close]
names_list = ["Least Squares Open", "Least Squares High", "Least Squares Low", "Least Squares Close"]
print_results(stats_list, names_list)
```

### :raised_hand_with_fingers_splayed: Visualize Results
```markdown
from HelperMethods.Helpers import plot_backtest_pnl, plot_backtest_distribution

plot_backtest_pnl(stats_list)
plot_backtest_distribution(stats_list)
```

## :raised_hand_with_fingers_splayed: Advanced Features

### :raised_hand_with_fingers_splayed: Pairs Trading
```
python code here
```

### :raised_hand_with_fingers_splayed: Optimization
```markdown
python code here
```

### :raised_hand_with_fingers_splayed: Monte Carlo Simulation
```markdown
python code here
```
