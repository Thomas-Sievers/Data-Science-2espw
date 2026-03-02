import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

#Show all the data frame
#print(df.to_string())

#Selection by column
#print(df["Name"].to_string())
#print(df['Height'].to_string())
#print(df[["Name", "Height", "Weight"]].to_string())

#Selection by row
#print(df.loc["Charizard"])
#print(df.loc["Geodude", ["Height", "Weight"]])
#print(df.loc["Pikachu" : "Jolteon", ["Height", "Weight"]])

#print(df.iloc[0:10])

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")