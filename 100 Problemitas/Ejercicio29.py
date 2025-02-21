"""
import numpy as np

import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')

plt.title('Histograma de Datos Aleatorios')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()
"""
def convertir_unidades(valor, unidad_origen, unidad_destino):
    conversiones = {
        'metros': {
            'kilometros': valor / 1000,
            'centimetros': valor * 100,
            'milimetros': valor * 1000
        },
        'kilometros': {
            'metros': valor * 1000,
            'centimetros': valor * 100000,
            'milimetros': valor * 1000000
        },
        'centimetros': {
            'metros': valor / 100,
            'kilometros': valor / 100000,
            'milimetros': valor * 10
        },
        'milimetros': {
            'metros': valor / 1000,
            'kilometros': valor / 1000000,
            'centimetros': valor / 10
        }
    }