import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Inicializar una matriz vacía
matriz = np.empty((filas, columnas), dtype=int)

####### SECCION A #######

# Solicitar al usuario ingresar valores para llenar la matriz
for i in range(filas):
    for j in range(columnas):
        if (((i+1)*(j+1))%2)==0:
            matriz[i, j] = (i+1)+(j+1)
        else:
            matriz[i, j] = (i+1)-(j+1)

# Mostrar la matriz
print("\nMatriz resultante:")
print(matriz)

print()
####### SECCION B #######

for i in range(filas):
    menor = matriz[i][0]
    posicion_j = 0
    for j in range(columnas):
        if menor>matriz[i][j]:
            menor = matriz[i][j]
            posicion_j = j
    print("Para la fila ",i+1,", resultara en la columna ",posicion_j+1,". Es decir: ",menor)
    
print()
####### SECCION C #######
for j in range(columnas):
    menor = matriz[0][j]
    posicion_i = 0
    for i in range(filas):
        if menor>matriz[i][j]:
            menor = matriz[i][j]
            posicion_i = j
    print("Para la columna ",j+1,", resultara en la fila ",posicion_i+1,". Es decir: ",menor)
 