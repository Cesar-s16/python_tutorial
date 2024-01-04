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

num=int(input('ingrese el numero a convertir a hexadecimal: '))
print('el numero en hexadecimal es: ', hexadecimal(num))