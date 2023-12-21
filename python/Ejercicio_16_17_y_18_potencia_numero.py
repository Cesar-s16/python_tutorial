#Ejercicio 16, 17 y 18 de la guía

num = int(input("Ingrese el numero: "))
potencia = int(input("Ingrese a que potencia va a elevarla: "))

if num == 0 and potencia == 0:
    print("Esto es una ideterminación")
elif num == 0 and potencia != 0:
    print(f"{num} elevado a la {potencia}, es igual a: 0")
elif num != 0 and potencia == 0:
    print(f"{num} elevado a la {potencia}, es igual a: 1")
else:
    resultado = 1
    for i in range(potencia):
        resultado = resultado * num
    print(f"{num} elevado a la {potencia}, es igual a: {resultado}")