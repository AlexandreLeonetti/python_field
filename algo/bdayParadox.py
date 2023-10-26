# birthday paradox
import math
import pandas as pd

p10= 1( - ((364 / 365) ** math.comb(10, 2))
p15=1 - ((364 / 365) ** math.comb(15, 2))

def birthday_probability(number_of_people):
    pass


df = pd.read_csv('nba_2017.csv', parse_dates=['Birth Date'])

df.head()
df['Birth Date'].dt.strftime("%Y-%m-%d").head()

