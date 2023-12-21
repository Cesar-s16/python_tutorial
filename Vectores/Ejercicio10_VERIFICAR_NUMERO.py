caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Verificar si el valor ASCII corresponde a un dígito
    if 48 <= valor_ascii <= 57:
        print(f"{caracter} es un dígito.")
    else:
        print(f"{caracter} no es un dígito.")
else:
    print("Por favor, ingresa solo un carácter.")
