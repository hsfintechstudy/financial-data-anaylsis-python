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
if __name__ == "__main__":
  main()

Add initial analysis script 
