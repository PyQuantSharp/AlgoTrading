import tkinter as tk 

def get_momentum_panel(tab):

    input_ticker = tk.Text(tab)
    input_ticker.pack()

    B = tk.Button(tab, text = "Enter")
    B.pack()

    return 0