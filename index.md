## Welcome to AlgoTrading

- Open source project dedicated to delivering high quality alpha
- Advanced, high performance backtesting engine
- Sponsored by Vicarisi Ventures, a quantitative development company
- To learn more, visit https://vicarisi.com/

### Getting Started 

The general steps are as followed: 

1. Initialize the Client: Object contains API Details
2. Fetch Historical Data with Client
3. Initialize Backtesting Parameters: Indicator Specifications
4. Compute Backtesting Indicators: Statistical Model, and Volatility
5. Initialize Statistics: Object contains insightful statistics
6. Compute Backtest Results: Returns PnL and Statistics Object
7. Print Scalar Statistics to Terminal
8. Visual Results: Distribution, PnL, Volatility 

### Initialize Client
Instantiate an object that wraps all variables needed to connect to the Tradier API
1. Paper Trading or Live Endpoint
2. API Key
3. Account ID
4. Ticker Symbol
5. Months to Grab Historical Data

```markdown
from Data.Client import Client

endpoint = "sandbox.tradier.com"
api_key = "ENTER API KEY"
accountid = "ENTER ACCOUNT ID"
ticker = "AAPL"
months = 60
client = Client(endpoint, api_key, accountid, ticker, months)
```

### Fetch Historical Data
Fetch historical data from Tradier and store in numpy arrays

1. Pass Client
2. Get OHLC price data
```markdown
from Data.Historical import get_historical_data

ohlc = get_historical_data(client)
```

### Initialize Backtesting Parameters
Instantiate object that wraps all variables needed to compute a backtest
1. Rolling Period
2. Indicator Projection

```markdown
from Indicators.Parameters import Parameters

period = 20
projection = 0
par = Parameters(period, projection)
```

### Compute Backtesting Indicators
Fetch statistical indicator
1. Pass Parameters, Price Data
2. Get Specified Indicator

```markdown

from Indicators.LeastSquares import get_least_squares

open = ohlc.open[period:]
high = ohlc.high[period:]
low = ohlc.low[period:]
close = ohlc.close[period:]

least_squares_average = get_least_squares(par, close)

```

### Initialize Statistics
Instantiate object that wraps all variables need to compute statistics
1. Pass Lot Size, Price Data
2. Get Statistics object

```markdown
from Backtesting.Statistics import Statistics

lot_size = 1
least_squares_open = Statistics(lot_size, len(open[period:]))
least_squares_high = Statistics(lot_size, len(high[period:]))
least_squares_low = Statistics(lot_size, len(low[period:]))
least_squares_close = Statistics(lot_size, len(close[period:]))
```

### Compute Backtest Results
Compute backtest results from  selected statistical indicator
1. Pass Statistics Object
2. Price Data
3. Indicator

```markdown
from Backtesting.Backtest import get_vanilla_backtest

least_squares_open = get_vanilla_backtest(least_squares_open, open[period:], least_squares_average)
least_squares_high = get_vanilla_backtest(least_squares_high, high[period:], least_squares_average)
least_squares_low = get_vanilla_backtest(least_squares_low, low[period:], least_squares_average)
least_squares_close = get_vanilla_backtest(least_squares_close, close[period:], least_squares_average)
```

### Print Statistics
Print statistics to terminal

```markdown
from HelperMethods.Helpers import print_results

stats_list = [least_squares_open, least_squares_high, least_squares_low, least_squares_close]
names_list = ["Least Squares Open", "Least Squares High", "Least Squares Low", "Least Squares Close"]
print_results(stats_list, names_list)
```

### Visualize Results
1. Distribution
2. PnL
3. Volatility

```markdown
from HelperMethods.Helpers import plot_backtest_pnl, plot_backtest_distribution

plot_backtest_pnl(stats_list)
plot_backtest_distribution(stats_list)
```

## Advanced Features

### Pairs Trading
```
python code here
```

### Optimization
```markdown
python code here
```

### Monte Carlo Simulation
```markdown
python code here
```
