numero_ingresado = int(input("Ingresa un número para verificar si es primo: "))
bandera = True

if 0 <= numero_ingresado <= 1:
    print(f"{numero_ingresado} No es n i primo ni compuesto")
    SystemExit
elif numero_ingresado == 2:
    print(f"{numero_ingresado} es un numero primo")
elif numero_ingresado < 0:
    print("No ingreses negativos")
    SystemExit
else:
    # Inicializamos el divisor en 3
        i = 3
        # Mientras el divisor sea menor o igual a la mitad del número
        while i <= numero_ingresado // 2:
            if numero_ingresado % i == 0:
                bandera = False
                break #Se acabó el problema
            # Incrementamos el divisor en 2, ya que ya hemos comprobado los pares
            i += 2

if bandera:
    print(f"{numero_ingresado} es un numero primo")
else:
    print(f"{numero_ingresado} es un numero compuesto")
    