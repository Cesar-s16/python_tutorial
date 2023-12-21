arreglo=[]
n=int(input('Ingrese la cantidad de elementos del arreglo: '))

for i in range(n):
    print('Posicion: ',i, end='. ')
    arreglo.append(int(input('ingrese un numero: ')))

sumap=0
sumai=0
contp=0
conti=0

for i in range(n):
    if (i%2)==0:
        sumap+=arreglo[i]
        contp+=1
    else:
        sumai+=arreglo[i]
        conti+=1

promp=sumap/contp
promi=sumai/conti

print("Promedio de numeros en posiciones pares: ", promp)
print("Promedio de numeros en posiciones impares: ", promi)