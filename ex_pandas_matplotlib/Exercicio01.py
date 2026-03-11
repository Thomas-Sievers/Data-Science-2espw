import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset_futebol.csv")
df.info()

min_500 = df[(df["Minutos_Jogados"] > 3000) & (df["Faltas_Cometidas"] < 7)]

posicao_mais_tempo = df.groupby("Posição")["Minutos_Jogados"].mean().round()
posicao_mais_tempo = posicao_mais_tempo.max()

jogador_assitencia = df.sort_values(by="Assistências", ascending=False).head(5)
jogador_assitencia = jogador_assitencia.iloc[0]
jogador_assitencia = jogador_assitencia["Nome_Jogador"]

x = df.Minutos_Jogados
y = df.Faltas_Cometidas
media_faltas = df["Faltas_Cometidas"].mean()

plt.scatter(x, y, color="Green")
plt.xlabel("Minutos jogados por cada jogador")
plt.ylabel("Faltas cometidas por cada jogador")
plt.axhline(y=media_faltas, color="Red", linestyle="--", label="Média de faltas" )
plt.title("Faltas cometidas por minutos jogados")
plt.legend()
plt.show()