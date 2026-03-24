import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_futebol.csv")

gols_por_posicao = df.groupby("Posição")["Gols_Marcados"].sum().reset_index()

posicoes = gols_por_posicao["Posição"]
total_gols = gols_por_posicao["Gols_Marcados"]

plt.bar(posicoes, total_gols)
plt.show()