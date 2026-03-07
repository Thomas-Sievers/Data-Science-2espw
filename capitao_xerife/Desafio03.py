import pandas as pd

df = pd.read_csv("datasets/dataset_003.csv")
#df.info()
#print(len(df))
#print(df.head(5))

idosos_magros = df[(df["Idade"] > 70) & (df["Peso_kg"] < 70)]
#Resultado disso deu 7
#print(len(idosos_magros))

homens = df.copy()
homens = homens.dropna(subset=["Paciente"])
homens = homens[homens["Sexo"].str.contains("M")]
#Resultado disso deu 17
#print(len(homens))

apenas_mulher = df[df["Sexo"] == "F"]
maior_mulher = apenas_mulher.sort_values(by="Alt_cm", ascending=False).head(1)
print(maior_mulher[["Paciente", "Alt_cm", "IMC"]])
maior_mulher_ICM = 35

linhas_completas = df.dropna()
#resultado disso deu 24
#print(len(linhas_completas))

soma_total = len(idosos_magros) + len(homens) + maior_mulher_ICM + len(linhas_completas)
print(soma_total)


