# Solicitamos al usuario que ingrese un número entero de 4 cifras
numero = int(input("Ingresa un número entero de 4 cifras: "))

# Verificamos si el número tiene exactamente 4 cifras
if 1000 <= numero <= 9999:
    # Calculamos las cifras individuales
    cifra_unidades = numero % 10
    cifra_decenas = (numero // 10) % 10
    cifra_centenas = (numero // 100) % 10
    cifra_millares = (numero // 1000) % 10

    # Calculamos la suma de los cuadrados de las cifras
    suma_cuadrados = cifra_unidades**2 + cifra_decenas**2 + cifra_centenas**2 + cifra_millares**2

    # Verificamos si el número es igual a la suma de los cuadrados de sus cifras
    if numero == suma_cuadrados:
        print(f"{numero} es igual a la suma de los cuadrados de sus cifras.")
    else:
        print(f"{numero} no es igual a la suma de los cuadrados de sus cifras.")
else:
    print("Por favor, ingresa un número de 4 cifras.")
