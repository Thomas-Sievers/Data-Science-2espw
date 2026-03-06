import pandas as pd

df = pd.read_csv("datasets/dataset_004.csv")
df.info()
#print(df.head(5))

severidade_alta_tempo_acima_60 = df[(df["Severidade"].str.contains("alta", case=False))
& (df["Tempo_min"] > 60)]
#Resultado disso deu 23
#print(len(severidade_alta_tempo_acima_60))

nao_estoura_SLA = df.copy()
nao_estoura_SLA = nao_estoura_SLA.dropna(subset=["Agente"])
nao_estoura_SLA = nao_estoura_SLA[nao_estoura_SLA["SLA_ok"].str.contains("SIM", case=False, na=False)]
#Resultado disso deu 98
#print(len(nao_estoura_SLA))

tempo_medio_atendimento = df.copy()
tempo_medio_atendimento = tempo_medio_atendimento.dropna(subset=["Tempo_min"])
tempo_medio_atendimento = tempo_medio_atendimento.groupby("Canal")["Tempo_min"].mean().round()
print(tempo_medio_atendimento)
tempo_medio_atendimento = tempo_medio_atendimento.max()
#Resultado disso deu 111
#print(tempo_medio_atendimento)

linhas_completas = df.dropna()
#print(len(linhas_completas))

soma_total = len(severidade_alta_tempo_acima_60) + len(nao_estoura_SLA) + tempo_medio_atendimento + len(linhas_completas)
print(soma_total)


