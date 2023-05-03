import pandas as pd
import pandas_ta as ta


class AddIndicators:
    def __init__(self, df, indicator_name):
        self.df = df
        if indicator_name == "RSI":
            self.rsi_ind()
        else:
            raise NotImplementedError("Other Indicators Are Not Implemented Yet!")
    
    def rsi_ind(self):
        self.df["RSI"] = ta.rsi(close=self.df["Close"])
        