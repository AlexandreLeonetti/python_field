# https://raposa.trade/blog/use-python-to-trade-the-donchian-channel/
# this program calculates donchian channel 
#https://www.youtube.com/watch?v=gtjxAH8uaP0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def indicator(data: pd.DataFrame, period: int):
      return data

#downloading the correct data from yahoo finance
ticker = "LTC-BTC"
yfObj = yf.Ticker(ticker) #returns data as panda dataframe.
data = yfObj.history(start="2020-10-01", end="2023-10-15").drop(
            ["Volume", "Stock Splits"], axis=1)
data = indicator(data, 10)
#print(data)
data.tail()
#print(data.info())
#print(data.shape)
#print(data.loc["2020-10-23"])
print(data.loc["2020-10-23","Open"])
print(data["Open"].max())
print(data.max())
print(data.describe())

print("*************")
df =data
df["ratio"]=(df["Open"]+df["Open"]-df["Close"])/df["Open"]

# Set "selected" column based on the condition
df.loc[df["ratio"] >= 0.59, "returns"] = df["ratio"]

# For rows where the condition is not met, set "selected" to 1.05
#df["selected"].fillna(1.05, inplace=True)
n_bins = 500

# Generate two normal distributions
dist1 = df["returns"]
fig, axs = plt.subplots(1,  tight_layout=True)

# We can set the number of bins with the *bins* keyword argument.
plt.hist(dist1, bins=n_bins)
#axs[1].hist(dist2, bins=n_bins)

# Add a vertical line at x = 1
plt.axvline(x=1, color='red', linestyle='--', label='x=1')
#axs[1].axvline(x=1, color='red', linestyle='--', label='x=1')
print(df)
plt.show()


def calcReturns(df):
    df["log_returns"] = np.log(df["returns"])
    df["cumulative_returns"] = np.exp(df["log_returns"].cumsum()) -1
    return df
calcReturns(df)
plt.figure(figsize=(12,4))
plt.plot(df["cumulative_returns"]*100, label="buy daily with SL")
plt.title("total returns test")
plt.xlabel("Date")
plt.ylabel("Returns (%)")
plt.xticks(rotation=45)
plt.show()

"""
"""      
