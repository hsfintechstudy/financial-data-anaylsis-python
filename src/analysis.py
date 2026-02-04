import pandas as pd 
import numpy as np 
import yfinance as yf 
import matplotlib.pyplot as plt 

def main(): 
  print("Financial data analysis project initialized.")
  ticker = "SPY" 
  start_date = "2018-01-01" 
  df = yf.download(ticker, start = start_date) 
  df = df.dropna()

  print(f"Downloaded {ticker} data from {start_date}")
  print(df.head())

  df["daily_return"] = df["Adj Close"].pct_change() 
  mean_return = df["daily_return"].mean()
  vol_return = df["daily_return"].std()

  print("\n--- Daily Return Summary ---") 
  print(f"Mean daily return: {mean_return:.6f}")
  print(f"Daily volatility (std): {vol_return:.6f}")

  cum_max = df["Adj Close"].cummax()
  drawdown = df["Adj Close"] / cum_max - 1
  mdd = drawdown.min()

  print(f"Maximum Drawdown (MDD) : {mdd:.2%}")

  df["Adj Close"].plot(title="SPY Adjusted Close Price") 
  plt.tight_layout()
  plt.savefig("spy_price.png")
  print("Saved plot: spy_price.png")
  

if __name__ == "__main__":
  main()


