import pandas as pd
import numpy as np

filename = "fatal-police-shootings-data.csv"
df = open(filename,"r")
dataframe = pd.read_csv(filename)
top = dataframe.head()
top

