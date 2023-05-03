import yfinance as yf


class DataReadYfinance:
    def __init__(self):
        self.data = None
        
    def get_data(self, symbol="EURUSD", time_frame="15m", duration="2d"):
        data = yf.download(symbol, interval=time_frame, period=duration)
        data['Date'] = data.index
        data = data.reset_index(drop=True)
        self.data = data[['Date', 'Open', 'High', 'Low', 'Close']]
        