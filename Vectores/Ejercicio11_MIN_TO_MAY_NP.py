letra_minuscula = input("Ingresa una letra minúscula: ")

# Verificar si la entrada es un solo carácter y si es una letra minúscula
if len(letra_minuscula) == 1 and 'a' <= letra_minuscula <= 'z':
    # Obtener el valor ASCII de la letra minúscula
    valor_ascii_minuscula = ord(letra_minuscula)
    
    # Calcular el valor ASCII de la letra mayúscula
    valor_ascii_mayuscula = valor_ascii_minuscula - 32
    
    # Obtener la letra mayúscula correspondiente
    letra_mayuscula = chr(valor_ascii_mayuscula)
    
    # Mostrar el resultado
    print(f"La letra mayúscula correspondiente es: {letra_mayuscula}")
else:
    print("Por favor, ingresa solo una letra minúscula.")
