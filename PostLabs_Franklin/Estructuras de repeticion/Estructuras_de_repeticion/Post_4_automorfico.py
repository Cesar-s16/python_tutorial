num = int(input("Numero a verificar si es automorfico: "))
veces = int(input("Numero de veces a hacer la iteración: "))
bandera = True
mult=1
aux=num
cantidad_digitos=0

while aux != 0:
    aux //= 10  # Eliminamos el último dígito
    cantidad_digitos += 1

for _ in range(0,cantidad_digitos):
    mult *= 10

print(f"{num} ** 1 = {num}")

for i in range(2,veces+1):    
    print(f"{num} ** {i} = {num**i}")
    
    if (num**i) % mult != num:
        bandera = False

if bandera:
    print("El numero es automorfico")
else:
    print("El numero NO es automorfico")