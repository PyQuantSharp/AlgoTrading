# Import Data Module
from Data.Client import Client
from Data.Historical import get_historical_data

# Import Statistical Indicators Module
from Indicators.Parameters import Parameters
from Indicators.LeastSquares import get_least_squares
from Indicators.DecisionTree import get_decision_tree
from Indicators.Ridge import get_ridge
from Indicators.BayesRidge import get_bayes_ridge

# Import Examples Module
from Examples.Individual import individual_backtest
from Examples.Pairs import pairs_backtest
from Examples.Optimized import optimized_backtest, optimized_pairs_backtest
from Examples.Live import live_trading

# Other Shit
import time 
import numpy as np
import matplotlib.pyplot as plt
from TickerSymbols import create_data_file, get_ticker_symbols

# Build Front End
import tkinter as tk 
from tkinter import ttk
from FrontEnd.MomentumPanel import get_momentum_panel
from FrontEnd.OptimizationPanel import get_optimization_panel
from FrontEnd.StatisticsPanel import get_statistics_panel

def backtest_example():

    isDisplay = True
    isContrarian = False

    # Multidimensional Array
    tickers = get_ticker_symbols()

    # Loop Thru All Tickers 
    for i in range(len(tickers)):

        # Compare Each Ticker to Each Ticker
        for j in range(len(tickers)):

            if i != j:

                # Store Data
                data = []

                # Step One: Initialize Client
                endpoint = "sandbox.tradier.com"
                api_key = "0qoGJZUqxFSc7zcBcAENRphluKVn"
                accountid = 0
                ticker = tickers[i][0]
                months = 60
                client = Client(endpoint, api_key, accountid, ticker, months)

                # Step Two: Fetch Historical Data
                ohlcA = get_historical_data(client)

                rolling_period = 10
                projection = 0
                # individual_backtest(ohlcA, rolling_period, projection, isDisplay, isContrarian)
                # print(tickers[i], ": Backtest Complete. ")

                ticker = tickers[j][0]
                client = Client(endpoint, api_key, accountid, ticker, months)
                ohlcB = get_historical_data(client)
                pairs_results = pairs_backtest(ohlcA, ohlcB, rolling_period, projection, isDisplay, isContrarian)
                print("tickers[i]", " ", tickers[j], ": Pairs Backtest Complete")

                data.append(tickers[i][0])
                data.append(tickers[j][0])
                data.append(np.sum(pairs_results[0].trade_results))
                data.append(pairs_results[0].win_rate)
                data.append(np.sum(pairs_results[1].trade_results))
                data.append(pairs_results[1].win_rate)
                data.append(np.sum(pairs_results[2].trade_results))
                data.append(pairs_results[2].win_rate)
                data.append(np.sum(pairs_results[3].trade_results))
                data.append(pairs_results[3].win_rate)
                
                print(data)
                create_data_file(data)

                # lower = 5
                # upper = 90
                # isDisplay = True
                # optimized_backtest(ohlcA, lower, upper, get_least_squares, projection, isDisplay, isContrarian)
                # optimized_pairs_backtest(ohlcA, ohlcB, lower, upper, get_least_squares, projection, isDisplay, isContrarian)
                # print(tickers[i], " ", tickers[j], ": Pairs Optimization Complete. ")

                print("Limiting API Calls")
                print("Sleeping...")
                time.sleep(2)

    # Limit Number of Charts
    if isDisplay == True:
        plt.show()

    # Create CSV File
    create_data_file(data)

    return 0

if __name__ == "__main__":        

    def main():

        window = tk.Tk()
        window.title("Vicarisi Ventures: Momentum Algo Trading")

        notebook = ttk.Notebook(window)
        notebook.pack()

        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)

        frame1.pack(fill = 'both', expand = True)
        frame2.pack(fill = 'both', expand = True)
        frame3.pack(fill = 'both', expand = True)

        notebook.add(frame1, text = 'Backtesting')
        notebook.add(frame2, text = 'Optimization')
        notebook.add(frame3, text = 'Statistics')

        get_momentum_panel(frame1)
        get_optimization_panel(frame2)
        get_optimization_panel(frame3)

        window.mainloop()

        return 0

    # Call Main Method
    main()







