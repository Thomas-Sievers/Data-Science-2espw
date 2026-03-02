import pandas as pd

df = pd.read_csv("pokemon.csv")

#Whole dataframe

#Calculate the arithmetic mean of each column.
print(df.mean(numeric_only=True))

#The sum of every register in each column
print(df.sum(numeric_only=True))

#The minimum of each column
print(df.min(numeric_only=True))

#The maximum of each column
print(df.max(numeric_only=True))

#Count the total registers of all column
print(df.count())

#Single column

#Calc the arithmetic mean of one column
print(df["Height"].mean())

#The sum of every register in a column
print(df["Height"].sum())

#The minimum of each column
print(df["Height"].min())

#The maximum of each column
print(df["Height"].max())

#Count the total registers of each column
print(df["Height"].count())

group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())