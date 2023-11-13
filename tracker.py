import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use("dark_background")


class Tracker:
    def __init__(self, stock_symbol: str, start, end:str=None):
        self.df = yf.download(stock_symbol, start=start, end=end)

    def add_metric(self, metric_name: str, metric_data: pd.Series):
        for col in self.df.columns:
            if col == metric_name:
                print("metric already exists")
                return
        self.df[metric_name] = metric_data

    def plot_separate(self, *metrics: str):
        fig, ax = plt.subplots(1, len(metrics), figsize=[24/len(metrics), 4])
        for i in range(len(metrics)):
            ax[i].plot(self.df[metrics[i]])
            ax[i].set_title(metrics[i])
        plt.show()

    def plot_group(self, *metrics: str):
        for i in range(len(metrics)):
            plt.plot(self.df[metrics[i]], label=metrics[i])
        plt.legend()
        plt.show()
