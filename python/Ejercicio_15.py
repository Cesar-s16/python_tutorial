numero = int(input("Ingresa un número entero (menor que 120): "))

if numero > 120:
    print("Lo siento, no se puede hacer eso.")
else:
    i=0
    while i < numero:
        j=0
        while j < i:
            print('-', end='')
            j += 1
        print('*')
        i += 1


'''if numero > 120:
    print("lo siento, no se puede hacer eso")
else:
    i=0
    while i<numero:    
        print('-' * i + '*')
        i += 1'''