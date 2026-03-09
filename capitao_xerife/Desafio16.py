import pandas as pd

df = pd.read_csv("datasets/dataset_016.csv")
df.info()

nota_8 = df[(df["Nota"] > 8) & (df["Presenca_%"] > 85)]
nota_8 = len(nota_8)

entrega_prazo = df.copy()
entrega_prazo = entrega_prazo.dropna(subset=["Aluno"])
entrega_prazo = entrega_prazo[entrega_prazo["Entrega_no_prazo"].str.contains("SIM", case=False, na=False)]
entrega_prazo = len(entrega_prazo)

maior_nota_turma = df.copy()
maior_nota_turma = maior_nota_turma.dropna(subset=["Nota"])
maior_nota_turma = maior_nota_turma.groupby("Turma")["Nota"].mean().round()
maior_nota_turma = maior_nota_turma.max()

maior_presenca = df.copy()
maior_presenca = maior_presenca.dropna(subset=["Presenca_%"])
maior_presenca = maior_presenca.sort_values(by="Presenca_%", ascending=False).head(5)
maior_presenca = maior_presenca["Nota"].iloc[0].round()


soma_total = nota_8 + entrega_prazo + maior_nota_turma + maior_presenca
print(soma_total)