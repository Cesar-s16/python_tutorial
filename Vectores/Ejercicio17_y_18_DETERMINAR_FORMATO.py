# Leer el número de cédula desde el teclado
numero_cedula = input("Ingrese el número de cédula: ")

# Verificar la longitud de la cédula
if len(numero_cedula) == 9:
    # Verificar si el primer carácter es 'V' o 'E'
    if numero_cedula[0] in ['V', 'E']:
        # Verificar si los siguientes 8 caracteres son dígitos
        todos_digitos = True
        for digito in numero_cedula[1:]:
            if not ('0' <= digito <= '9'):
                todos_digitos = False
                break
        
        if todos_digitos:
            print(f"Cédula válida ({'Venezolana' if numero_cedula[0] == 'V' else 'Extranjera'})")
        else:
            print("Cédula inválida")
    else:
        print("Cédula inválida")
else:
    print("Cédula inválida")
