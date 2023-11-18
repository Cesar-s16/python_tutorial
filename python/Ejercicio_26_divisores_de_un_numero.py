num = int(input("Ingresa un número entero positivo: "))

if num <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    print(f"Los divisores de {num} son:")
    for i in range(1, num+1):
        if num % i == 0:
            print(f"{i}. ", end= " ")
