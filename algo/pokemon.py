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

# find most powerful pokemon by Total  where Type 1 or Type 2 == Dragon from gen 1 and 2
df.loc[
            ((df["Type 1"] == "Dragon" ) |    (df["Type 2"] == "Dragon")) 
                &
                    (df["Generation"].isin({5,6}))
                    ]


df.loc[
            ((df["Type 1"] == "Dragon" ) | 
                     (df["Type 2"] == "Dragon")) 
                &
                    (df["Generation"].isin({5,6}))
                    ].sort_values(by="Total", ascending=False)


# select all pokemons that have an Attack value above 100 and Type 1 == Fire 9ignore Type 2
powerful_fire_df =df.loc[(df["Type 1"]=="Fire") & (df["Attack"]> 100)]

# select all pokemons of Type 1 == Water & Type 2 == Flying, 
water_flying_df = df.loc[(df["Type 1"]=="Water")&(df["Type 2"]=="Flying")]
# select all Legendary where Type 1 == Fire, only select cloumn Name, Attack, Generation
#legendary_fire_df = 
df.loc[(df["Legendary"]==True)&(df["Type 1"]=="Fire"),["Name","Attack","Generation"]]

# some plot :
ax = df['Speed'].plot(kind='hist', figsize=(10, 5), bins=100)
ax.axvline(df['Speed'].quantile(.05), color='red')
ax.axvline(df['Speed'].quantile(.95), color='red')

df.loc[
        (CONDITION FOR INDEX),
        (COLUMNS)
        ]


# select both 5% extremums of pokemons according to speed
bottom_5 = df["Speed"].quantile(.05)
top_5    = df["Speed"].quantile(.95)
#(bottom_5,top_5)

slow_fast_df = df.loc[(df["Speed"]<bottom_5)|(df["Speed"]>top_5)]

#16
df.loc[(df["Attack"]>140)&(df["Defense"]>130)&(df["Legendary"]==True)]
#other answer
df.loc[df["Legendary"]].sort_values(by=["Attack", "Defense"], ascending = False]
