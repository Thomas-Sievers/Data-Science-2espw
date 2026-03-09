import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Criando dados: 7 dias da semana x 6 períodos do dia
dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
horas = ["Manhã", "Tarde", "Noite", "Madrugada", "Almoço", "Happy Hour"]
#Radint creates numbers from 0 to 49             Create a 2D matrix with 7 rows and 6 columns
vendas = np.random.randint(0, 50, (7,6))

#Creates a whiteboard with a width of 8 inches and a height of 5 inches
plt.figure(figsize=(8,5))
#            print the numbers  Sets the pallet  Change the labels of X and Y axis
sns.heatmap(vendas, annot=True, cmap="coolwarm", xticklabels=horas, yticklabels=dias)

plt.title("Heatmap de vendas por dia e período")
plt.xlabel("Período do dia")
plt.ylabel("Dia da semana")
plt.show()