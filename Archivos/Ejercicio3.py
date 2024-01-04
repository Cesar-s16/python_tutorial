def hexadecimal(num):
    hex=''
    while num>0:
        if num%16==10:
            hex='A'+ hex
        elif num%16==11:
            hex='B'+ hex
        elif num%16==12:
            hex='C'+ hex
        elif num%16==13:
            hex='D'+ hex
        elif num%16==14:
            hex='E'+ hex
        elif num%16==15:
            hex='F'+ hex
        else:
            hex= str(num%16) + hex
        num=num//16
    return hex

def guardar_hexadecimal_en_archivo(hex):
    nombre = 'Prueba.txt'
    with open(nombre, 'w') as archivo:
        archivo.write(hex)

def leer_hexadecimal_desde_archivo():
    nombre = 'Prueba.txt'
    try:
        with open(nombre, 'r') as archivo:
            hex = archivo.read()
        return hex
    except FileNotFoundError:
        print("El archivo '", nombre, "' no existe.")
        return None

num=int(input('ingrese el numero a convertir a hexadecimal: '))
hex=hexadecimal(num)
guardar_hexadecimal_en_archivo(hex)
print("numero en hexadecimal proveniente del archivo: ", leer_hexadecimal_desde_archivo())
