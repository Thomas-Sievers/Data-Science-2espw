import pandas as pd

df = pd.read_csv("dataset_001.csv")

df.info()
print(df.head(5))

compras_acima_500 = df[(df["Valor_R$"] > 500) & (df["Entrega_dias"] > 10)]
#Resultado disso da 32
#print(len(compras_acima_500))

cupom_sem_cidade = df.copy()
cupom_sem_cidade = cupom_sem_cidade.dropna(subset=["Cidade"])
cupom_sem_cidade = df[df["Cupom"].str.contains("SIM", case=False)]
#Resultado disso deu 55
#print(len(cupom_sem_cidade))

produto_media_alta = df.copy()
produto_media_alta = produto_media_alta.groupby("Categoria")['Valor_R$'].mean().round()
#Resultado deu 672
print(produto_media_alta)

sem_NaN = df.copy()
sem_NaN = sem_NaN.dropna()
#Resultado deu 77
print(len(sem_NaN))

soma_total = len(compras_acima_500) + len(cupom_sem_cidade) + produto_media_alta["Valor_R$"].max() + len(sem_NaN)
print(soma_total)

