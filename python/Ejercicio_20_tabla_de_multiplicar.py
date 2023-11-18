num = int(input("Ingrese el numero para generar su tabla de multicar (entre 1 y 10): "))

if 1 <= num <= 10:
    i=0
    while i<=10:
        print(f"{num} x {i} = {num*i}")
        i += 1
else:
    print("No está en el rango")