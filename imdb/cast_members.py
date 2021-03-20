import numpy as np
import pandas as pd

df = pd.read_csv("imdb.csv", sep=",", '''names = ["year", "week", "date", "hit5", "hit4", "hit3", "hit2","num1",
 "num2", "num3", "num4", "num5"]''')

num = df[["num1","num2", "num3", "num4", "num5"]].copy()
numbers = num.to_numpy().flatten()
print(len(numbers))

new_series = pd.Series(numbers)
print("The most frequent numbers: \n",new_series.value_counts()[0:5])
print("The most frequent number: \n",new_series.value_counts().idxmax())


print(num.head())
print(num.describe())