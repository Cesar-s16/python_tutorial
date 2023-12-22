def byte_ascii(byte_input):
    # Verificar si la entrada es una cadena de bytes
    if len(byte_input) == 1 and byte_input.isascii():
        # Obtener el valor ASCII del byte ingresado
        valor_ascii = ord(byte_input)
        
        # Mostrar el resultado
        print(f"El valor ASCII correspondiente al byte ingresado es: {valor_ascii}")
    else:
        print("La entrada no es un byte ASCII válido.")

# Leer un byte desde el teclado
byte_input = byte_ascii(input("Ingresa un byte (en formato ASCII): "))