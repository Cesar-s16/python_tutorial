def sig_valor(valor_ascii):
    # Calcular el valor ASCII del siguiente carácter
    siguiente_valor_ascii = valor_ascii + 1
    
    # Obtener el carácter correspondiente al siguiente valor ASCII
    return chr(siguiente_valor_ascii)

caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Mostrar el resultado
    print(f"El carácter siguiente en la tabla ASCII es: {sig_valor(valor_ascii)}")
else:
    print("Por favor, ingresa solo un carácter.")
