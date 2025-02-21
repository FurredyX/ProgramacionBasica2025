import numpy as np

import matplotlib.pyplot as plt

# Generar datos aleatorios
data = np.random.randn(1000)

# Crear el histograma
plt.hist(data, bins=30, edgecolor='black')

# Añadir título y etiquetas
plt.title('Histograma de Datos Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()