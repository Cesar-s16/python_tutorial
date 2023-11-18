num_a = int(input("Ingresa el primer número entero: "))
num_b = int(input("Ingresa el segundo número entero: "))

# Comparamos los números y mostramos el resultado
if num_a > num_b:
    print(f"{num_a} es mayor que {num_b}.")
elif num_a < num_b:
    print(f"{num_a} es menor que {num_b}.")
else:
    print(f"{num_a} es igual a {num_b}.")