texto = input("Ingresa un texto: ")

# Calcular la cantidad de espacios en el string
cont=0
for i in texto:
    if i==" ":
        cont+=1

# Mostrar el resultado
print(f"El texto ingresado tiene {cont} caracteres.")
