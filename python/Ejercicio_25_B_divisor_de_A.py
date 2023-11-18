a = int(input("Ingresa un número entero positivo (A): "))
b = int(input("Ingresa otro número entero positivo (B): "))

if b == 0:
    print("No se puede dividir por cero.")
elif a % b == 0:
    print(f"{b} es un divisor de {a}.")
else:
    print(f"{b} no es un divisor de {a}.")