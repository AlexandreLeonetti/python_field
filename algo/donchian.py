# https://raposa.trade/blog/use-python-to-trade-the-donchian-channel/
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

#downloading the correct data from yahoo finance
ticker = "DOGE-USD"
yfObj = yf.Ticker(ticker)
data = yfObj.history(start="2021-07-01", end="2022-08-01").drop(
            ["Volume", "Stock Splits"], axis=1)
data = calcDonchianChannels(data, 10)
data.tail()

# plotting the donchian chart
colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.figure(figsize=(12, 8))
plt.plot(data["Close"], label="Close", linewidth=0.5)
plt.plot(data["upperDon"], label="Upper", c=colors[1], linewidth=0.5)
plt.plot(data["lowerDon"], label="Lower", c=colors[4], linewidth=0.5)
plt.plot(data["midDon"], label="Mid", c=colors[2], linestyle=":", linewidth=0.5)
plt.fill_between(data.index, data["upperDon"], data["lowerDon"], alpha=0.3,
                 color=colors[1])

plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title(f"Donchian Channels for {ticker}")
plt.xticks(rotation=45)
plt.legend()
plt.show()


# strategy :


def midDonCrossOver(data: pd.DataFrame, period: int=10, shorts: bool=True):
  data = calcDonchianChannels(data, period)

  data["position"] = np.nan
  data["position"] = np.where(data["Close"]>data["midDon"], 1, 
                              data["position"])
  if shorts:
    data["position"] = np.where(data["Close"]<data["midDon"], -1, 
                                data["position"])
  else:
    data["position"] = np.where(data["Close"]<data["midDon"], 0, 
                                data["position"])
  data["position"] = data["position"].ffill().fillna(0)

  return calcReturns(data)




# Here are a few helper functions to give us returns and summary stats
def calcReturns(df):
  df['returns'] = df['Close'] / df['Close'].shift(1)
  df['log_returns'] = np.log(df['returns'])
  df['strat_returns'] = df['position'].shift(1) * df['returns']
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



midDon = midDonCrossOver(data.copy(), 10, shorts=False)

plt.figure(figsize=(12, 4))
plt.plot(midDon["strat_cum_returns"] * 100, label="Mid Don X-Over")
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
