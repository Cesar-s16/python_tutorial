num = int(input("Ingresa un número entero positivo: "))
suma = 0
if num <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    for i in range(1, (num//2)+1):
        if num % i == 0:
            suma = suma + i
    print(suma)

if suma == num:
    print(f"El  numero {num} es perfecto")
else:
    print(f"El numero {num} NO es perfecto")