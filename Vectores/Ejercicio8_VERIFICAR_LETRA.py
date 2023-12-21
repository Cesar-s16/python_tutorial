caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Verificar si el valor ASCII corresponde a una letra
    if (65 <= valor_ascii <= 90) or (97 <= valor_ascii <= 122):
        print(f"{caracter} es una letra.")
    else:
        print(f"{caracter} no es una letra.")
else:
    print("Por favor, ingresa solo un carácter.")
