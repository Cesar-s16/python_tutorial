num_a = int(input("Ingresa el primer número entero positivo: "))
num_b = int(input("Ingresa el segundo número entero positivo: "))

if num_a <= 0 or num_b <= 0:
    print("Por favor, los dos numeros deben ser positivos")
else:
    #Sumar los digitos del primero numero
    suma_a = 0
    for i in range(1, (num_a//2)+1):
        if num_a % i == 0:
            suma_a = suma_a + i
    
    #Sumar los digitos del primero numero
    suma_b = 0
    for j in range(1, (num_b//2)+1):
        if num_b % j == 0:
            suma_b = suma_b + j
    
    #VERIFICAMOS
    if suma_a == num_b and suma_b == num_a:
        print(f"Los numeros {num_a} y {num_b} son Amigos")
    else:
        print(f"Los numeros {num_a} y {num_b} NO son Amigos")