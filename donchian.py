# this program calculates donchian channel 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def calcDonchianChannels(data: pd.DataFrame, period: int):
      data["upperDon"] = data["High"].rolling(period).max()
      data["lowerDon"] = data["Low"].rolling(period).min()
      data["midDon"] = (data["upperDon"] + data["lowerDon"]) / 2
      return data

