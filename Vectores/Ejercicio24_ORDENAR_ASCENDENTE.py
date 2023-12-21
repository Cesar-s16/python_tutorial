arreglo=[]
n=int(input('Ingrese la cantidad de elementos del arreglo: '))

for i in range(n):
    print('Posicion: ',i, end='. ')
    arreglo.append(int(input('ingrese un numero: ')))

# Algoritmo de ordenamiento de burbuja para ordenar el arreglo de manera ascendente
for i in range(n):
    for j in range(0, n-i-1):
        if arreglo[j] > arreglo[j+1]:
            # Intercambiar los elementos si están en el orden incorrecto
            arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

# Mostrar el arreglo ordenado
print("Arreglo ordenado de manera ascendente:", arreglo)