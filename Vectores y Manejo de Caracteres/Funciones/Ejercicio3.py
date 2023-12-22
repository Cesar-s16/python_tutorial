def verificar_valor(valor_entero):
    if 0 <= valor_entero <= 255:
        return True
    else:
        return False

valor_entero = input("Ingresa un valor entero entre 0 y 255: ")

# Verificar si la entrada es un número entero
if valor_entero.isdigit():
    valor_entero = int(valor_entero)
    
    # Verificar si el valor está en el rango permitido
    if verificar_valor(valor_entero):
        # Obtener el carácter ASCII correspondiente
        caracter_ascii = chr(valor_entero)
        
        # Mostrar el resultado
        print(f"El carácter ASCII correspondiente al valor {valor_entero} es: {caracter_ascii}")
    else:
        print("El valor ingresado no está en el rango permitido.")
else:
    print("La entrada no es un número entero válido.")
