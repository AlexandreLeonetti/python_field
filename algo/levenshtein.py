#levenshtein

import itertools
import pandas as pd

# The new library!
from thefuzz import fuzz, process

df1 = pd.read_csv('companies_1.csv')
df2 = pd.read_csv('companies_2.csv')


