# https://raposa.trade/blog/use-python-to-trade-the-donchian-channel/
# this program calculates donchian channel 
#https://www.youtube.com/watch?v=gtjxAH8uaP0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def indicator(data: pd.DataFrame, period: int):
      return data

#downloading the correct data from yahoo finance
ticker = "LTC-USD"
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

# print the value of several rows
#print(data.loc[["2020-10-23","2020-11-23","2021-10-03"]])
#print(data.loc[["2020-10-23","2020-11-23","2021-10-03"],"Open"])
#print(data.sort_values(by=["Open"], ascending=False))
# first conditional statements :
#print(data.loc[data["Open"] >= 300])
#print(data["Open"].value_counts().head())
df =data
#print(data.loc[df["Open"] >= 93].head(10))
print(data.loc[df["Open"] <= 93].sample(10))

#print(df.loc[df["Open"] >= 250].sort_values(by="High"))
print(df.loc[(df["Open"] <= 300)&(df["High"] >= 300)].sort_values(by="High"))

df["ratio"]=df["Close"]/df["Open"]
print(df.sample(10))

print(df["ratio"].max())
print(df.sort_values(by="ratio", ascending=False).head(10))

print(df.loc[df["ratio"] == df["ratio"].max()])

print(df.loc[df["ratio"] >= 1.1].shape)
print(df.query("ratio >= 1.1"))
print(df.query("ratio >= 1.1").sort_values(by="Open", ascending=False))
