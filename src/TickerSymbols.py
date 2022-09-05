import pandas as pd
import numpy as np

def get_ticker_symbols():
    """
    Read Tickers Symbols CSV and convert to Numpy Array
    """

    df = pd.read_csv('QQQTickers.csv')
    ticker_array = df.to_numpy()

    return ticker_array

def create_data_file(pairs_backtests):

    df = pd.DataFrame([pairs_backtests])

    df.columns =[
        'Ticker A',
        'Ticker B',
        'Open PnL', 
        'Open Win Rate',
        'High PnL', 
        'High Win Rate',
        'Low PnL', 
        'Low Win Rate',
        'Close PnL', 
        'Close Win Rate',] 

    df.to_csv("PairsBacktest.csv", sep = '\t', encoding = 'utf-8', index = False) 

    return 0
    