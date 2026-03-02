import pandas as pd

#Dictionary
data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [20, 30, 40],
}

#Creating DataFrame with the values of the dictionary
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

#Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

#Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["Employee 4"])
df = pd.concat([df, new_row])

#Add new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])

print(df)