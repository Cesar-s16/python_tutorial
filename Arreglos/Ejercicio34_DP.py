import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
rango = int(input("Ingrese la cantidad de filas y columnas: "))

# Inicializar una matriz vacía
matriz = np.empty((rango, rango), dtype=int)

# Solicitar al usuario ingresar valores para llenar la matriz
cont=0
for i in range(rango):
    for j in range(rango):
        if i==j:
            cont+=1
            matriz[i][j]=cont
        else:
            matriz[i][j]=0

# Mostrar la matriz
print("\nMatriz resultante:")
print(matriz)