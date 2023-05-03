import pandas as pd


class TradingStrategy:
    def __init__(self, data, strategy):
        self.data = data
        if strategy == "RSI-30buy-50sell":
            self.rsi_30buy_50sell()
        else:
            raise NotImplementedError("This Strategy Is Not Implemented Yet!")
            
    def rsi_30buy_50sell(self):
        entry_date = None
        for candle in range(len(self.data)):
            if not entry_date and self.data["RSI"].iloc[candle] < 30:
                entry_date = self.data["Date"].iloc[candle]
                print(f"Entered to a Buy Position at: {entry_date} and at price: {self.data['Close'].iloc[candle]} \
                                                                   and at RSI Value of {self.data['RSI'].iloc[candle]}")
            
            if entry_date and self.data["RSI"].iloc[candle] > 50:
                entry_date = None
                print(f"Exited from Position at {self.data['Date'].iloc[candle]} and at price: {self.data['Close'].iloc[candle]} \
                                                                            and at RSI Value of {self.data['RSI'].iloc[candle]}")
                print("**************** WAITING FOR THE NEXT POSITION ******************")
                print("")
             
    