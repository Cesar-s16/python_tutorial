letra_minuscula = input("Ingresa una letra minúscula: ")

# Verificar si la entrada es un solo carácter y si es una letra minúscula
if len(letra_minuscula) == 1 and letra_minuscula.islower():
    # Utilizar la función upper() para convertir a mayúscula
    letra_mayuscula = letra_minuscula.upper()
    
    # Mostrar el resultado
    print(f"La letra mayúscula correspondiente es: {letra_mayuscula}")
else:
    print("Por favor, ingresa solo una letra minúscula.")
