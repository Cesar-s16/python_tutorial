a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))

a_absoluto = abs(a)
b_absoluto = abs(b)

resultado = a_absoluto

for _ in range(b_absoluto-1):
    resultado = resultado + a_absoluto

if (a < 0 and b > 0) or (a > 0 and b < 0):
        resultado = -resultado

print(f"El producto de {a} y {b} es: {resultado}")