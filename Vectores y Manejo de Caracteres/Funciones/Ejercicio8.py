def es_letra(valor_ascii):
    if (65 <= valor_ascii <= 90) or (97 <= valor_ascii <= 122):
        return "es una letra."
    else:
        return "no es una letra."

caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Verificar si el valor ASCII corresponde a una letra
    print(caracter,"",es_letra(valor_ascii))
else:
    print("Por favor, ingresa solo un carácter.")
