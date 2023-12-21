import numpy as np
matriz = np.array([[9,4,5], [0,3,7], [8,1,2]])

# Recorrer la matriz
filas=3
columnas=3

print("Recorriendo la matriz:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i, j], end=" ")
    print()  # Salto de línea después de cada fila