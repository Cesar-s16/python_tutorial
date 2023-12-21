texto = input("Ingresa un texto: ")

i=0
tope=len(texto)
aux=tope-1
band = True

while i < (tope//2):
    if texto[i]!=texto[aux]:
        band = False
    aux-=1
    i+=1

if band:
    print("Es palindromo")
else:
    print("No es palindromo")