def vocal_a_mayuscula(oracion):
    cadena=''
    for i in oracion:
        if i=='a':
            cadena+='A'
        elif i=='e':
            cadena+='E'
        elif i=='i':
            cadena+='I'
        elif i=='o':
            cadena+='O'
        elif i=='u':
            cadena+='U'
        else:
            cadena+=i
    return cadena

def procesar_y_actualizar_archivo(nombre_archivo):
    try:
        # Leer el contenido actual del archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido_original = archivo.read()

        # Procesar la cadena y convertir las vocales a mayúsculas
        contenido_modificado = vocal_a_mayuscula(contenido_original)

        # Escribir la cadena resultante al final del archivo
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido_modificado)

        print(f"Se ha procesado y actualizado el archivo '{nombre_archivo}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

# Ejemplo de uso
nombre_archivo = "cadena.txt"

# Procesar y actualizar el archivo
procesar_y_actualizar_archivo(nombre_archivo)
