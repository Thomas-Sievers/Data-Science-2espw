import pandas as pd

data = [100, 102, 103, 200, 202]

#Creating a data frame  | Renaming the index
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

#Changing the value of index c
series.loc["c"] = 200

#Outputting only the value of index a
print(series.loc["a"])

#Even with renamed index, we can still access them by their original label
print(series.iloc[0])

#Only output values greater than 200 (inside the series)
print(series[series >= 200])




