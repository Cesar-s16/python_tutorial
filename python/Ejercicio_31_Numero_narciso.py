num = int(input("Ingresa un número entero positivo: "))

if num <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    suma = 0
    numero = num
    while numero > 0:
        # Obtenemos el dígito más a la derecha
        digito = numero % 10
        
        #Elevamos el digitos a la 3
        digito = digito**3

        # Sumamos el dígito a la suma total
        suma += digito

        # Eliminamos el dígito más a la derecha del número
        numero //= 10

    print(f"La suma de los dígitos es: {suma}")
    
    if num == suma:
        print(f"{num} es un numero Narciso")
    else:
        print(f"{num} NO es un numero Narciso")
