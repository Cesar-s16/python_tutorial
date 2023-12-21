arreglo=[]
n=int(input('Ingrese la cantidad de elementos del arreglo: '))

for i in range(n):
    print('Posicion: ',i, end='. ')
    arreglo.append(int(input('ingrese un numero: ')))

mayor = arreglo[0]

for i in range(n):
    if arreglo[i]>mayor:
        mayor = arreglo[i]

print("El numero mayor en la lista de numeros es: ", mayor)