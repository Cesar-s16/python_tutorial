import numpy as np

# Solicitar al usuario la cantidad de filas y columnas
rango = int(input("Ingrese la cantidad de filas y columnas: "))
if rango>0:
    # Inicializar una matriz vacía
    matriz = np.empty((rango, rango), dtype=int)

    # Solicitar al usuario ingresar valores para llenar la matriz
    for j in range(rango):
        for i in range(rango):
            print("posicion: ",i,",",j)
            matriz[i, j] = int(input("Ingrese los datos de la posicion: "))

    #Cantidd de elementos de la matriz
    cantidad = rango*rango

    # Sumar los elementos de la matriz
    suma = 0
    for j in range(rango):
        for i in range(rango):
            suma+=matriz[i, j]
    
    promedio = suma/cantidad
    
    print("El promedio de la matriz es de: ", promedio)
else:
    print("La matriz esta vacia, no se puede aplicar promedio")