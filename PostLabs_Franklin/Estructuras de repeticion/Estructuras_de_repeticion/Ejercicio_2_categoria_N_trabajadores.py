i=1
while True:
    nombre = str(input(f"Ingrese nombre del trabajador {0}: "))
    print("Ingrese el cargo del travajador")
    print("[1] Para Instructor")
    print("[2] Para Asistente")
    print("[3] Para Agregado")
    print("[4] Para Asociado")
    print("[5] Para Titular")
    
    cargo = int(input("Cargo: "))
    while cargo<1 and cargo>5: 
        print("Por favor, ingrese un valor valido")
        cargo = int(input("Cargo: "))            
            
    sueldo = int(input("Ingrese su sueldo: "))
    
    if cargo == 1:
        sueldo = sueldo * 1.4
        print(f"Nuevo sueldo del trabajador {nombre}, con un cargo de Instructor, seria: {sueldo}")
    elif cargo == 2:
        sueldo = sueldo * 1.35
        print(f"Nuevo sueldo del trabajador {nombre}, con un cargo de Asistente, seria: {sueldo}")
    elif cargo ==3:
        sueldo = sueldo * 1.25
        print(f"Nuevo sueldo del trabajador {nombre}, con un cargo de Agregado, seria: {sueldo}")
    elif cargo == 4:
        sueldo = sueldo * 1.20
        print(f"Nuevo sueldo del trabajador {nombre}, con un cargo de Asociado, seria: {sueldo}")
    elif cargo == 5:
        sueldo = sueldo * 1.20
        print(f"Nuevo sueldo del trabajador {nombre}, con un cargo de Titular, seria: {sueldo}")
    
    i += 1
    
    respuesta = input("¿Desea seguir ingresando trabajadores? [S]: Si, [N]: No. ")
    while respuesta.lower() != "s" and respuesta.lower() != "n":
        print("Por favor, ingrese un valor válido")
        respuesta = input("¿Desea seguir ingresando trabajadores? [S]: Si, [N]: No")

    if respuesta == "N":
        break