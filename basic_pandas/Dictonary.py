import pandas as pd

calories = {'Day 1': 1750, "Day 2": 2100, "Day 3": 1700}

#Series is just a column
series = pd.Series(calories)

#Change of the value of a index Day 3
series.loc["Day 3"] += 500

print(series[series < 2000])