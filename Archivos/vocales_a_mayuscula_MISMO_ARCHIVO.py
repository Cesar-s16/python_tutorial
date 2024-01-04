def leer_hexadecimal_desde_archivo():
    nombre = 'oracion2.txt'
    try:
        with open(nombre, 'r') as archivo:
            hex = archivo.read()
        return hex
    except FileNotFoundError:
        print("El archivo '", nombre, "' no existe.")
        return None
    
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

def guardar_hexadecimal_en_archivo(cadena):
    nombre = 'oracion2.txt'
    try:
        with open(nombre, 'a') as archivo:
            archivo.write("\n" + cadena)
        return hex
    except FileNotFoundError:
        print("El archivo '", nombre, "' no existe.")
        return None

#guardar_hexadecimal_en_archivo(vocal_a_mayuscula(leer_hexadecimal_desde_archivo()))
oracion=leer_hexadecimal_desde_archivo()
cadena=vocal_a_mayuscula(oracion)
guardar_hexadecimal_en_archivo(cadena)
print("programa finalizado")