# https://raposa.trade/blog/use-python-to-trade-the-donchian-channel/
# this program calculates donchian channel 
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
"""
# plotting the donchian chart
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.figure(figsize=(12, 8))
plt.plot(data["Close"], label="Close", linewidth=0.5)
plt.plot(data["highDon"], label="Upper", c=colors[1], linewidth=0.5)
plt.plot(data["lowerDon"], label="Lower", c=colors[4], linewidth=0.5)
plt.plot(data["midDon"], label="Mid", c=colors[2], linestyle=":", linewidth=0.5)
plt.fill_between(data.index, data["highDon"], data["lowerDon"], alpha=0.3,
                 color=colors[1])

plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title(f"Donchian Channels for {ticker}")
plt.xticks(rotation=45)
plt.legend()
plt.show()
"""

# strategy :


def strategy(data: pd.DataFrame, period: int=10, shorts: bool=True):
  data = indicator(data, period)
  
  data["position"] = np.nan # initialization of the whole column at NaN
  data["position"] = np.where(data["Open"]>0,1, 0) # assign 1 to range and 0 to rest print (data)
  print(data)
  for a in data["Open"]:
      print(a)

  for i,a in data["position"]:
      data["position"][i] = 2
  print(data)
  #data["position"] = np.where(np.logical_and(data.index>="2020-10-02 00:00:00+00:00",data.index<="2021-05-05 00:00:00+00:00"),1, 0) # assign 1 to range and 0 to rest
  #data["position"] = np.where(np.logical_and(data.index>="2021-07-01 00:00:00+00:00",data.index<="2021-11-05 00:00:00+00:00"),1, data["position"]) #assign 1 to range2 and previous values to rest
  #data["position"] = np.where(np.logical_and(data.index>="2022-07-02 00:00:00+00:00",data.index<="2023-07-05 00:00:00+00:00"),1, data["position"]) # assign 1 to range3 and previous values to rest
  #data["position"] = data["position"].ffill().fillna(0)

  return calcReturns(data)




# Here are a few helper functions to give us returns and summary stats
def calcReturns(df):
  df['returns'] = df['Close'] / df['Close'].shift(1) # calculate returns from a day's close to the next.(while position is held)
  #print(df)
  df['log_returns'] = np.log(df['returns'])
  df['strat_returns'] = df['position'].shift(1) * df['returns']
  #print(df)
  df['strat_log_returns'] = df['position'].shift(1) * \
      df['log_returns']
  df['cum_returns'] = np.exp(df['log_returns'].cumsum()) - 1
  df['strat_cum_returns'] = np.exp(
      df['strat_log_returns'].cumsum()) - 1
  df['peak'] = df['cum_returns'].cummax()
  df['strat_peak'] = df['strat_cum_returns'].cummax()
  return df

def getStratStats(log_returns: pd.Series,
  risk_free_rate: float = 0.02):
  stats = {}  # Total Returns
  stats['tot_returns'] = np.exp(log_returns.sum()) - 1  
  
  # Mean Annual Returns
  stats['annual_returns'] = np.exp(log_returns.mean() * 252) - 1  
  
  # Annual Volatility
  stats['annual_volatility'] = log_returns.std() * np.sqrt(252)
  
  # Sortino Ratio
  annualized_downside = log_returns.loc[log_returns<0].std() * \
    np.sqrt(252)
  stats['sortino_ratio'] = (stats['annual_returns'] - \
    risk_free_rate) / annualized_downside  
  
  # Sharpe Ratio
  stats['sharpe_ratio'] = (stats['annual_returns'] - \
    risk_free_rate) / stats['annual_volatility']  
  
  # Max Drawdown
  cum_returns = log_returns.cumsum() - 1
  peak = cum_returns.cummax()
  drawdown = peak - cum_returns
  max_idx = drawdown.argmax()
  stats['max_drawdown'] = 1 - np.exp(cum_returns[max_idx]) \
    / np.exp(peak[max_idx])
  
  # Max Drawdown Duration
  strat_dd = drawdown[drawdown==0]
  strat_dd_diff = strat_dd.index[1:] - strat_dd.index[:-1]
  strat_dd_days = strat_dd_diff.map(lambda x: x.days).values
  strat_dd_days = np.hstack([strat_dd_days,
    (drawdown.index[-1] - strat_dd.index[-1]).days])
  stats['max_drawdown_duration'] = strat_dd_days.max()
  return {k: np.round(v, 4) if type(v) == np.float_ else v
          for k, v in stats.items()}


midDon = strategy(data.copy(), 10, shorts=False)

plt.figure(figsize=(12, 4))
plt.plot(midDon["strat_cum_returns"] * 100, label="Strategy")
plt.plot(midDon["cum_returns"] * 100, label="Buy and Hold")
plt.title("Cumulative Returns for Mid Donchian Cross-Over Strategy")
plt.xlabel("Date")
plt.ylabel("Returns (%)")
plt.xticks(rotation=45)
plt.legend()

plt.show()

stats = pd.DataFrame(getStratStats(midDon["log_returns"]), 
                     index=["Buy and Hold"])
stats = pd.concat([stats,
                   pd.DataFrame(getStratStats(midDon["strat_log_returns"]),
                               index=["MidDon X-Over"])])
stats




"""

40-50k par an
"""
