#https://app.datawars.io/project/54b07e96-f0da-4b5d-ba40-c87475e42b8e?page=1
#https://www.youtube.com/watch?v=gtjxAH8uaP0
#starts  at 33 min


# methods in this project:
# df.loc, df.iloc, df.query, df.sort_values

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")

df.head()

df.info()
df.describe()
df['Type 1'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='tab20c', figsize=(10, 8))
df['Total'].plot(kind='hist', figsize=(10, 8))
df['Total'].plot(kind='box', vert=False, figsize=(10, 5))
df['Legendary'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='Set3', figsize=(10, 8))
sns.boxplot(data=df, x='Attack')

# Try your code here
# check how many pokemon with attack >= 150
sns.boxplot(data=df, x='Speed')
df.loc[df["Attack"] > 150]
(df["Attack"] >150).sum()# result 3

#Select all pokemons with a Speed of `10` or less
# select pokemon with sp def < 25
(df["Sp. Def"] <= 25).sum()
# Try your code here
# list all pokemons that are Legendary
legendary_df = df.loc[df["Legendary"]==True]
# ~ tilde is the equivalent of not operator (turns False into True)
# some scatter plot :
ax = sns.scatterplot(data=df, x="Defense", y="Attack")
ax.annotate(
            "Who's this guy?", xy=(228, 10), xytext=(150, 10), color='red',
                arrowprops=dict(arrowstyle="->", color='red')
)


# find the outlier pokemon
# find pokemons that are both type Fire nd Flying
((df["Type 1"]=="Fire" )& (df["Type 2"]=="Flying")).sum()

# using the or operator
((df["Type 1"]=="Poison" ) | (df["Type 2"]=="Poison")).sum()



#What pokemon of Type 1 Ice has the strongest defense?
df.loc[(df["Type 1"] == "Ice") &
               (df["Defense"] == df.loc[df["Type 1"] == "Ice", "Defense"].max())
                     ]

#other answer
df.loc[df["Type 1"] == "Ice"].sort_values("Defense", ascending = False)

# count each type, type with highest count among Legendary is the answer
df.loc[df["Legendary"],"Type 1"].value_counts().plot(kind="bar")

# most powerful pokemon by Total from the first 3 gen that is of type water.
df.loc[(df["Generation"]<=3)&(df["Type 1"]=="Water")].sort_values("Total", ascending = False)


