num = int(input("ingrese numero al que se le va a aplicar factorial: "))
i=1
fact = 1

while i<=num:
    fact *= i
    i+=1

print(f"El factorial de {num} es: {fact}")