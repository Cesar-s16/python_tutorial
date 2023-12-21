texto = input("Ingresa un texto: ")

# Calcular la cantidad de caracteres en el string
cantidad_caracteres = len(texto)

# Mostrar el resultado
print(f"El texto ingresado tiene {cantidad_caracteres} caracteres.")

# Otra forma
cont=0
for i in texto:
    cont+=1

# Mostrar el resultado
print(f"El texto ingresado tiene {cont} caracteres.")
