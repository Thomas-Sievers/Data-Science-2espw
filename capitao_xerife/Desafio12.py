import pandas as pd

df = pd.read_csv("datasets/dataset_012.csv")
# df.info()

atraso_15 = df[(df["Atraso_min"] > 15) & (df["Preco_R$"] < 25)]
atraso_15_valor = len(atraso_15)

pago_pix = df.copy()
pago_pix = pago_pix.dropna(subset=["Regiao"])
pago_pix = pago_pix[pago_pix["Pagamento"].str.contains("Pix", case=False)]
pago_pix_valor = len(pago_pix)

dist = df.copy()
dist = dist.dropna(subset=["Dist_km"])
maior_dist = dist["Dist_km"].max()
dist = dist[dist["Dist_km"] == maior_dist]
valor_dist = dist["Preco_R$"].max().round()

atraso_medio = df.copy()
atraso_medio = atraso_medio.dropna(subset=["Atraso_min"])
atraso_medio = atraso_medio.groupby("Regiao")["Atraso_min"].mean().max().round()

soma_total = atraso_15_valor + pago_pix_valor + valor_dist + atraso_medio
print(soma_total)






