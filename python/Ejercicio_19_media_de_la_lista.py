cont = 0
sum = 0
while True:
    num = int(input("Ingrese un numero, para salir: "))
    if num >= 0:
        cont += 1
        sum = sum + num
    else:
        prom = sum/cont
        print(f"El promedio de la lista es de: {prom:.2f}")
        break