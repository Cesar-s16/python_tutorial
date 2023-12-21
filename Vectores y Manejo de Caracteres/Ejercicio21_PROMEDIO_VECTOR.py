# Solicitar al usuario que ingrese elementos al arreglo
arreglo_enteros = []
n = int(input("Ingrese la cantidad de elementos en el arreglo: "))
suma=0

if n>0:
    for i in range(n):
        print("Posicion ",i,". ", end='')
        elemento = int(input("Ingrese un número entero: "))
        arreglo_enteros.append(elemento)
        suma+=arreglo_enteros[i]

    # Calcular el promedio
    promedio = suma / n
    print(f"El promedio del arreglo es: {promedio}")
else:
    print("El arreglo está vacío. No se puede calcular el promedio.")
