numero_ingresado = int(input("Ingresa un número entero: "))

numero = numero_ingresado + 1
while True:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        break
    numero += 1

print(f"El próximo número primo más grande que {numero_ingresado} es: {numero}")
