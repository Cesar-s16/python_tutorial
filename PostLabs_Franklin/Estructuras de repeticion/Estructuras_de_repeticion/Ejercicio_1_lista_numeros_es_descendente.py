bandera = True
num = int(input("Ingrese un numero, para terminar ingrese 0: "))
menor = num

while True:   
    if num==0:
        break
    elif num > menor:
        bandera = False
    else:
        menor = num
    
    num = int(input("Ingrese un numero, para terminar ingrese 0: "))

if bandera:
    print("La lista es descendente")
else:
    print("La lista NO es descendete")