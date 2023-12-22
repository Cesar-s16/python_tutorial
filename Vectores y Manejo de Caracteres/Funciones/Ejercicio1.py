def ascii (carcater):
    # Obtener el valor ASCII del caracter ingresado
    valor_ascii = ord(caracter)
    return valor_ascii

caracter = input("Ingresa un caracter: ")

# Mostrar el resultado
print(f"El valor ASCII de '{caracter}' es: {ascii(caracter)}")
