import numpy as np
import pandas as pd

df = pd.read_csv("imdb.csv", sep=',', converters = {'cast':lambda x:x.split(',')})
df2 = df[["cast"]].copy()
cast = df2.to_numpy().flatten()
cast_series = pd.Series(cast)
cast_series =  cast_series.apply(pd.Series).stack().reset_index(drop = True)
most_frequent = cast_series.value_counts()[0:5]
most_frequent.to_csv('cast.csv')
