tope = int(input("Ingresar tope de iteraciones de la Serie de Fibonacci: "))

if tope<0:
    print("Lo siento, esta serie no está disponible")
elif tope==0:
    print("1.")
else:
    i=0
    a=0
    b=1
    print("1.", end= " ")
    while i<tope:
        c=b+a
        print(f"{c}.", end= " ")
        a=b
        b=c
        i += 1
        
    