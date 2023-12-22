def promedio(n):
    arreglo_enteros = []
    suma=0
    
    for i in range(n):
        print("Posicion ",i,". ", end='')
        elemento = int(input("Ingrese un número entero: "))
        arreglo_enteros.append(elemento)
        suma+=arreglo_enteros[i]

    # Calcular el promedio
    return suma / n

# Solicitar al usuario que ingrese elementos al arreglo
n = int(input("Ingrese la cantidad de elementos en el arreglo: "))

if n>0:
    print(f"El promedio del arreglo es: {promedio(n)}")
else:
    print("El arreglo está vacío. No se puede calcular el promedio.")
