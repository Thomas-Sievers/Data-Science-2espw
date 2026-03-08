import pandas as pd

df = pd.read_csv("datasets/dataset_001.csv")
df.info()

vlr_500 = df[(df["Valor_R$"] > 500) & (df["Entrega_dias"] > 10)]
vlr_500 = len(vlr_500)

compras_cupom = df.copy()
compras_cupom = compras_cupom.dropna(subset=["Cidade"])
compras_cupom = compras_cupom[compras_cupom["Cupom"].str.contains("SIM", case=False, na=False)]
compras_cupom = len(compras_cupom)

produto_maior_vlr = df.copy()
produto_maior_vlr = produto_maior_vlr.dropna(subset=["Valor_R$"])
produto_maior_vlr = produto_maior_vlr.groupby("Categoria")["Valor_R$"].mean().round()
#This is wrong because the .mean() function automatically sort the values alphabetically, not by number
#produto_maior_vlr = produto_maior_vlr.iloc[0]
produto_maior_vlr = produto_maior_vlr.max()

linhas_completas = df.copy()
linhas_completas = linhas_completas.dropna()
linhas_completas = len(linhas_completas)

soma_total = vlr_500 + compras_cupom + produto_maior_vlr + linhas_completas
print(soma_total)

