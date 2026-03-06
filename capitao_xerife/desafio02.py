import pandas as pd

df = pd.read_csv("datasets/dataset_002.csv")

#df.info()
#print(df.head(5))

nota_presenca = df[(df["Nota"] > 8) & (df["Presenca_%"] > 85)]
#Resultado deu 3
#print(len(nota_presenca))

entrega_prazo = df.copy()
entrega_prazo = entrega_prazo.dropna(subset=["Aluno"])
entrega_prazo = entrega_prazo[entrega_prazo["Entrega_no_prazo"].str.contains("SIM", case=False)]
#Resutado deu 47
#print(len(entrega_prazo))

nota_media_turma = df.copy()
nota_media_turma = nota_media_turma.dropna(subset=["Nota"])
nota_media_turma = nota_media_turma.groupby("Turma")["Nota"].mean().round()
nota_media_turma = nota_media_turma.max()
#Resultado deu 6
#print(nota_media_turma)

maior_presenca = df.copy()
maior_presenca = maior_presenca.dropna(subset=["Presenca_%"])
maior_presenca = maior_presenca[maior_presenca["Presenca_%"] == 100]
#Resultado disso deu 6
maior_presenca = maior_presenca[["Presenca_%", "Nota"]].max().round()
#print(maior_presenca)

soma_total = len(nota_presenca) + len(entrega_prazo) + nota_media_turma + maior_presenca["Nota"]
print(soma_total)