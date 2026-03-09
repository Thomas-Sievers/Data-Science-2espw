import pandas as pd

from desafio02 import soma_total

df = pd.read_csv("datasets/dataset_020.csv")
df.info()

vlr_500 = df[(df["Valor_R$"] > 500) & (df["Entrega_dias"] > 10)]
vlr_500 = len(vlr_500)

compras_cupom = df.copy()
compras_cupom = compras_cupom.dropna(subset=["Cidade"])
compras_cupom = compras_cupom[compras_cupom["Cupom"].str.contains("SIM", case=False)]
compras_cupom = len(compras_cupom)

produto_vlr_medio = df.copy()
produto_vlr_medio = produto_vlr_medio.dropna(subset=["Valor_R$"])
produto_vlr_medio = produto_vlr_medio.groupby("Categoria")["Valor_R$"].mean().round()
produto_vlr_medio = produto_vlr_medio.max()

linhas_completas = df.copy()
linhas_completas = linhas_completas.dropna()
linhas_completas = len(linhas_completas)

soma_total = vlr_500 + compras_cupom + produto_vlr_medio + linhas_completas
print(soma_total)