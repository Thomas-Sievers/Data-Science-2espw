import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file
df = pd.read_csv("partidas_brasil_copa22.csv")
df.info()

#Get the average of brazil goals
media_gols = df["Gols_Brasil"].mean()
print(media_gols)

x = df.Gols_Brasil

#Line chart  Mark every match  Give it a label
plt.plot(x, marker="o", label="Gols por partida")
#This add the orange line, it's the average of goals
plt.axhline(y=media_gols, color="orange", linestyle="--", label="Média de Gols")
plt.xlabel("Gols do Brasil")
plt.ylabel("Número da partida (Índice)")
plt.title("Gols feito pelo time do Brasil por partida")
#Show all labels
plt.legend()
plt.show()

#Bar chart
adversarios = df.Adversario
gols_marcados = df.Gols_Brasil

plt.figure(figsize=(20, 6))
plt.bar(adversarios, gols_marcados)
plt.show()