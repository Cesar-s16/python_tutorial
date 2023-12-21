texto = input("Ingresa un texto: ")
nuevo_texto =''
# Cambiar todas las vocales a mayusculas
for i in texto:
    if i=="a" or i=='e' or i=='i' or i=='o' or i=='u':
        nuevo_texto+=i.upper()
    else:
        nuevo_texto+=i

print(nuevo_texto)