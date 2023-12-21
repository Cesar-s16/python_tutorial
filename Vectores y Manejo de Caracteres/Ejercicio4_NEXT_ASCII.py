caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Calcular el valor ASCII del siguiente carácter
    siguiente_valor_ascii = valor_ascii + 1
    
    # Obtener el carácter correspondiente al siguiente valor ASCII
    siguiente_caracter = chr(siguiente_valor_ascii)
    
    # Mostrar el resultado
    print(f"El carácter siguiente en la tabla ASCII es: {siguiente_caracter}")
else:
    print("Por favor, ingresa solo un carácter.")
