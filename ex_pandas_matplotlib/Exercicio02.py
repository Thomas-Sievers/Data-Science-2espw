import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_futebol.csv")
df.info()

media_altura = df["Altura_cm"].mean()

plt.hist(df.Altura_cm, bins=10, edgecolor="black")
plt.axvline(x=media_altura, linestyle="--", color="red")
plt.show()