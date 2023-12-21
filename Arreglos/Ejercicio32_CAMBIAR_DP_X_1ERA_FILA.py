import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
rango = int(input("Ingrese la cantidad de filas y columnas: "))
if rango>0:
    # Inicializar una matriz vacía
    matriz = np.empty((rango, rango), dtype=int)

    # Solicitar al usuario ingresar valores para llenar la matriz
    for i in range(rango):
        for j in range(rango):
            print("posicion: ",i,",",j)
            matriz[i, j] = int(input("Ingrese los datos de la posicion: "))

    print(matriz)
    
    print()
    matriz2 = matriz.copy()
    #Matriz cambiada
    
    for i in range(rango):
        matriz2[0][i]=matriz[i][i]
        matriz2[i][i]=matriz[0][i]
    
    print(matriz2)
else:
    print("Invalido")