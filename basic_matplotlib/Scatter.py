import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color="blue")
plt.xlabel("Variável X")
plt.ylabel("Variável Y")
plt.title("Exemplo de scatter plot")
plt.show()