import pandas as pd

df = pd.read_csv("datasets/dataset_011.csv")
df.info()

acima_70 = df[(df["Idade"] > 70) & (df["Peso_kg"] < 70)]
acima_70 = len(acima_70)

masculino = df.copy()
masculino = masculino.dropna(subset=["Paciente"])
masculino = masculino[masculino["Sexo"].str.contains("M", case=False, na=False)]
masculino = len(masculino)

maior_feminino = df.copy()
maior_feminino = maior_feminino[maior_feminino["Sexo"].str.contains("F", case=False, na=False)]
maior_feminino = maior_feminino.sort_values(by="Alt_cm", ascending=False)
#This is wrong because .head() returns a panda series
#maior_feminino = maior_feminino["IMC"].head(1)
maior_feminino = maior_feminino["IMC"].iloc[0]

linhas_completas = df.copy()
linhas_completas = linhas_completas.dropna()
linhas_completas = len(linhas_completas)

soma_total = acima_70 + masculino + maior_feminino + linhas_completas
print(soma_total)
