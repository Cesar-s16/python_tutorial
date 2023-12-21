arreglo=[]
n=int(input('Ingrese la cantidad de elementos del arreglo: '))

for i in range(n):
    print('Posicion: ',i, end='. ')
    arreglo.append(int(input('ingrese un numero: ')))

posiciones=[]
cont=0
dentro=int(input("Ingrese que numero va a verificar si esta en el arreglo"))

for i in range(n):
    band = False
    
    if arreglo[i]==dentro:
        band = True
    
    if band:
        cont+=1
        posiciones.append(i)

print("El numero ",dentro," sse encuentra en el arreglo", cont, "veces")
print("Se encuentra en las posiciones: ",posiciones)