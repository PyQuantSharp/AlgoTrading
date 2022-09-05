import numpy as np

# Import Backtesting Module
from Backtesting.Indicators import PairsIndicators
from Backtesting.Indicators import Indicators
from Backtesting.Variables import Statistics
from Backtesting.Backtest import get_vanilla_backtest
from Backtesting.PairsBacktest import get_pairs_backtest

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Volatility Module
from Volatility.VolClusters import get_vol_clusters

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters

from Correlation.CorrelationClusters import get_corr_clusters
from Examples.Volatility import plot_vol_metrics

def brute_force_optimization(a, b, ohlc, indicator, projection, isContrarian):
    """
    Returns the PnL of an interval of rolling periods

    Input:
    1. Lower Bound, Ex: 30 days
    2. Upper Bound, Ex: 90 days
    3. Price Data
    4. Statistical Indicator

    Output:
    1. The PnL per each rolling period
    """

    open_pnl = np.zeros(b - a)
    high_pnl = np.zeros(b - a)
    low_pnl = np.zeros(b - a)
    close_pnl = np.zeros(b - a)

    for i in range(b - a):

        period = a + i
        par = Parameters(period, projection)

        # Volatility Clusters
        VS = get_vol_clusters(ohlc, period)

        open = ohlc.open[period:]
        high = ohlc.high[period:]
        low = ohlc.low[period:]
        close = ohlc.close[period:]

        long_cluster = 0
        short_cluster = 2
        moving_average = indicator(par, close)
        IndicatorsObj = Indicators(moving_average, VS.cvol, VS.cvol_clusters, VS.cvol_vol, VS.cvol_vol_clusters, long_cluster, short_cluster)

        lot_size = 1
        indicator_open = Statistics(lot_size, len(open[period:]), period)
        indicator_high = Statistics(lot_size, len(high[period:]), period)
        indicator_low = Statistics(lot_size, len(low[period:]), period)
        indicator_close = Statistics(lot_size, len(close[period:]), period)

        indicator_open = get_vanilla_backtest(indicator_open, open[period:], IndicatorsObj, isContrarian)
        indicator_high = get_vanilla_backtest(indicator_high, high[period:], IndicatorsObj, isContrarian)
        indicator_low = get_vanilla_backtest(indicator_low, low[period:], IndicatorsObj, isContrarian)
        indicator_close = get_vanilla_backtest(indicator_close, close[period:], IndicatorsObj, isContrarian)

        open_pnl[i] = np.sum(indicator_open.trade_results)
        high_pnl[i] = np.sum(indicator_high.trade_results)
        low_pnl[i] = np.sum(indicator_low.trade_results)
        close_pnl[i] = np.sum(indicator_close.trade_results)

    return open_pnl, high_pnl, low_pnl, close_pnl

def brute_force_pairs_optimization(a, b, ohlcA, ohlcB, indicator, projection, isContrarian):
    """
    Returns the PnL of an interval of rolling periods

    Input:
    1. Lower Bound, Ex: 30 days
    2. Upper Bound, Ex: 90 days
    3. Price Data
    4. Statistical Indicator

    Output:
    1. The PnL per each rolling period
    """

    open_pnl = np.zeros(b - a)
    high_pnl = np.zeros(b - a)
    low_pnl = np.zeros(b - a)
    close_pnl = np.zeros(b - a)

    for i in range(b - a):

        period = a + i
        par = Parameters(period, projection)

        # Volatility Clusters
        VSA = get_vol_clusters(ohlcA, period)
        VSB = get_vol_clusters(ohlcB, period)
        CS = get_corr_clusters(ohlcA, ohlcB, period)

        openA = ohlcA.open[period:]
        highA = ohlcA.high[period:]
        lowA = ohlcA.low[period:]
        closeA = ohlcA.close[period:]

        openB = ohlcB.open[period:]
        highB = ohlcB.high[period:]
        lowB = ohlcB.low[period:]
        closeB = ohlcB.close[period:]

        # Calculate Indicators
        long_cluster = 1
        short_cluster = 1
        least_squares_averageA = indicator(par, closeA)
        least_squares_averageB = indicator(par, closeB)
        IndicatorsObj = PairsIndicators(least_squares_averageA, least_squares_averageB, 
                                        VSA.cvol, VSA.cvol_clusters, VSA.cvol_vol, VSA.cvol_vol_clusters, 
                                        VSB.cvol, VSB.cvol_clusters, VSB.cvol_vol, VSB.cvol_vol_clusters, 
                                        CS.ccorr, CS.ccorr_clusters, CS.ccorr_vol, CS.ccorr_vol_clusters, 
                                        long_cluster, short_cluster)

        lot_size = 1
        least_squares_open = Statistics(lot_size, len(openA[period:]), period)
        least_squares_high = Statistics(lot_size, len(highA[period:]), period)
        least_squares_low = Statistics(lot_size, len(lowA[period:]), period)
        least_squares_close = Statistics(lot_size, len(closeA[period:]), period)

        least_squares_open = get_pairs_backtest(least_squares_open, openA[period:], openB[period:], IndicatorsObj, isContrarian)
        least_squares_high = get_pairs_backtest(least_squares_high, highA[period:], highB[period:], IndicatorsObj, isContrarian)
        least_squares_low = get_pairs_backtest(least_squares_low, lowA[period:], lowB[period:], IndicatorsObj, isContrarian)
        least_squares_close = get_pairs_backtest(least_squares_close, closeA[period:], closeB[period:], IndicatorsObj, isContrarian)

        open_pnl[i] = np.sum(least_squares_open.trade_results)
        high_pnl[i] = np.sum(least_squares_high.trade_results)
        low_pnl[i] = np.sum(least_squares_low.trade_results)
        close_pnl[i] = np.sum(least_squares_close.trade_results)

    return open_pnl, high_pnl, low_pnl, close_pnl