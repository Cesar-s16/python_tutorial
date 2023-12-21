# Programa para verificar si un carácter es mayúscula, minúscula o no es una letra usando ASCII

# Leer un carácter desde el teclado
caracter = input("Ingresa un carácter: ")

# Verificar si la entrada es un solo carácter
if len(caracter) == 1:
    # Obtener el valor ASCII del carácter
    valor_ascii = ord(caracter)
    
    # Verificar si el carácter es mayúscula
    if 65 <= valor_ascii <= 90:
        print(f"{caracter} es una letra mayúscula.")
    # Verificar si el carácter es minúscula
    elif 97 <= valor_ascii <= 122:
        print(f"{caracter} es una letra minúscula.")
    # Si no es mayúscula ni minúscula, entonces no es una letra
    else:
        print(f"{caracter} no es una letra.")
else:
    print("Por favor, ingresa solo un carácter.")
