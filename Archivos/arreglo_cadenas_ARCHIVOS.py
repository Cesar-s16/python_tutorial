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

def ingresar_arreglo_en_archivo(nombre_archivo, arreglo):
    with open(nombre_archivo, 'w') as archivo:
        for elemento in arreglo:
            archivo.write(elemento + '\n')

def leer_y_modificar_archivo(nombre_archivo_entrada, nombre_archivo_salida):
    try:
        # Leer el contenido actual del archivo
        with open(nombre_archivo_entrada, 'r') as archivo_entrada:
            contenido_original = archivo_entrada.read().splitlines()

        # Modificar cada elemento del arreglo
        contenido_modificado = []
        for elemento in contenido_original:
            elemento_modificado = vocal_a_mayuscula(elemento)
            contenido_modificado.append(elemento_modificado)

        with open(nombre_archivo_salida, 'w') as archivo_salida:
            for elemento_modificado in contenido_modificado:
                archivo_salida.write(elemento_modificado + '\n')

        print(f"Se ha leído y modificado el archivo '{nombre_archivo_entrada}'.")
        print(f"El resultado se ha guardado en el archivo '{nombre_archivo_salida}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo_entrada}' no existe.")

# Ejemplo de uso
nombre_archivo_entrada = "arreglo.txt"
nombre_archivo_salida = "arreglo2.txt"

# Ingresar un arreglo de strings en el archivo
arreglo_ingreso = ["hola", "mundo", "python", "ejemplo", "amigo", "querido"]
ingresar_arreglo_en_archivo(nombre_archivo_entrada, arreglo_ingreso)

# Leer y modificar el archivo
leer_y_modificar_archivo(nombre_archivo_entrada, nombre_archivo_salida)
