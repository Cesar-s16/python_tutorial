texto = input("Ingresa un texto: ")

tope=len(texto)
aux=tope-1
band = True

for i in range(tope//2):
    if texto[i]!=texto[aux]:
        band = False
    aux-=1

if band:
    print("Es palindromo")
else:
    print("No es palindromo")