import matplotlib.pyplot as plt

#Criando um gráfico de linha simples
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.title("Meu Primeiro Gráfico")
plt.show()