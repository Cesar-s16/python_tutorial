texto = input("Ingresa un texto: ")

# Calcular la cantidad de espacios en el string
conta=0
conte=0
conti=0
conto=0
contu=0
contTotalVocales=0
for i in texto:
    if i=="a" or i=="A":
        conta+=1
        contTotalVocales+=1
    elif i=='e' or i=='E':
        conte+=1
        contTotalVocales+=1
    elif i=='i' or i=='I':
        conti+=1
        contTotalVocales+=1
    elif i=='o' or i=='O':
        conto+=1
        contTotalVocales+=1
    elif i=='u' or i=='U':
        contu+=1
        contTotalVocales+=1

# Mostrar el resultado
print(f"El texto ingresado tiene {conta} veces la letra ¨A¨.")
print(f"El texto ingresado tiene {conte} veces la letra ¨E¨.")
print(f"El texto ingresado tiene {conti} veces la letra ¨I¨.")
print(f"El texto ingresado tiene {conto} veces la letra ¨O¨.")
print(f"El texto ingresado tiene {contu} veces la letra ¨U¨.")
print(f"El texto ingresado tiene {contTotalVocales} vocales.")