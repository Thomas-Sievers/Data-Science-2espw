import pandas as pd

#Read the csv file
df = pd.read_csv("pokemon.csv")

#Show firsts n columns
df.head(3)