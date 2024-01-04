def binario(num):
    bin=''
    while num>0:
        if num%2==0:
            bin='0'+bin
        else:
            bin='1'+bin
        num=num//2
    return bin

num=int(input('ingrese el numero a convertir a binario: '))
print('el numero en binario es: ', binario(num))