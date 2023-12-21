import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
rango = int(input("Ingrese la cantidad de filas y columnas: "))

# Inicializar una matriz vacía
matriz = np.empty((rango, rango), dtype=int)

# Solicitar al usuario ingresar valores para llenar la matriz
for i in range(rango):
    for j in range(rango):
        print("posicion: ",i,",",j)
        matriz[i, j] = int(input("Ingrese los datos de la posicion: "))

# Mostrar la matriz
print("\nMatriz resultante:")
print(matriz)
