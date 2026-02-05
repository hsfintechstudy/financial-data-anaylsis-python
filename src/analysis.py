import pandas as pd 
import numpy as np 
import yfinance as yf 
import matplotlib.pyplot as plt


def main(): 
  print("Financial data analysis project initialized.")
  ticker = "SPY" 
  start_date = "2018-01-01" 
  df = yf.download(ticker, start = start_date, auto_adjust=False, group_by="column")
  price_col = "Adj Close" if "Adj Close" in df.columns else "Close"
  df["daily_return"] = df[price_col].pct_change()

  df = df.dropna()

  print(f"Downloaded {ticker} data from {start_date}")
  print(df.tail())

  # Pick price column safely
  price_col = "Adj Close" if "Adj Close" in df.columns else "Close"

  df["daily_return"] = df[price_col].pct_change()
  mean_return = df["daily_return"].mean()
  vol_return = df["daily_return"].std()

  print("\n--- Daily Return Summary ---") 
  print(f"Mean daily return: {mean_return:.6f}")
  print(f"Daily volatility (std): {vol_return:.6f}")

  cum_max = df[price_col].cummax()
  drawdown = df[price_col] / cum_max - 1
  mdd = drawdown.min().iloc[0]

  print(f"Maximum Drawdown (MDD) : {mdd:.2%}")

  df[price_col].plot(title=f"{ticker} {price_col} Price") 
  plt.tight_layout()
  plt.savefig("spy_price.png")
  print("Saved plot: spy_price.png")
  plt.show()



if __name__ == "__main__":
  main()


