tope = int(input("ingrese el tope de la serie: "))
i=0
suma=0

print("0.", end=" ")

for i in range(tope):
    suma = suma + 3
    print(f"{suma}.", end=" ")
    i += 1
