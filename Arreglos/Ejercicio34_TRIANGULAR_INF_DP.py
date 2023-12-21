import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
rango = int(input("Ingrese la cantidad de filas y columnas: "))

# Inicializar una matriz vacía
matriz = np.empty((rango, rango), dtype=int)

# Diagonal Principal
for i in range(rango):
    for j in range(rango):
            matriz[i][j]=0

# Triangular Superior con Diagonal Principal
for i in range(rango):
    for j in range(0, i+1):
            matriz[i][j]=1

# Mostrar la matriz
print("\nMatriz resultante:")
print(matriz)