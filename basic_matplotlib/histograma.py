import matplotlib.pyplot as plt
import numpy as np

dados = np.random.randn(1000)

plt.hist(dados, bins=20, edgecolor='black')
plt.show()